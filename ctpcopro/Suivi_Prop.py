from selectolax.parser import HTMLParser
from datetime import datetime
import sqlite3
import re
import sys
from typing import Any
from rich.console import Console
from rich.table import Table
from loguru import logger

console = Console()

db_path = "ctpcopro/coproprietaires.sqlite"
logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    colorize=True,
    serialize=False,
    backtrace=True,
    diagnose=True,
)

logger.warning("Début du script de suivi des copropriétaires")
logger.info("Chargement du fichier HTML")

# Charger le contenu du fichier HTML
with open(
    "ctpcopro\\Extranet du cabinet CSJC _ Accès Copropriétaire.htm",
    "r",
    encoding="utf-8",
) as file:
    html_content = file.read()

# Parser le contenu HTML avec Selectolax
parser = HTMLParser(html_content)


def recuperer_date_situation_copro(HTMLParser: HTMLParser) -> str:
    """
    Extrait la date de la situation des copropriétaires à partir d'un noeud HTML spécifié.

    La fonction recherche une balise "td" avec l'identifiant "lzA1" dans le document HTML,
    extrait le texte de la balise, nettoie le texte pour faciliter la recherche,
    et extrait la date au format JJ/MM/AAAA après le motif spécifié.

    Parameters:
    - HTMLParser (HTMLParser): Un objet HTMLParser contenant le document HTML à analyser.

    Returns:
    - str: La date extrait au format JJ/MM/AAAA.
    """
    node = parser.css_first("td#lzA1")
    if node:
        texte = node.text()
        # Normaliser le texte pour faciliter la recherche
        texte_normalise = re.sub(r"\s+", " ", texte)
        # Extraire uniquement la date au format JJ/MM/AAAA après "Solde des copropriétaires au"
        match = re.search(
            r"Solde des copropriétaires au\s+(\d{2}/\d{2}/\d{4})", texte_normalise
        )
        if match:
            date_str = match.group(1)
            print(f"Date trouvée : {date_str}")
        else:
            print("Date non trouvée dans la balise lzA1.")
    else:
        print("Balise td#lzA1 non trouvée.")

    date_situation_copro = datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    last_check_situation_copro = datetime.now().strftime("%Y-%m-%d")
    return date_situation_copro, last_check_situation_copro


def recuperer_situation_copro(
    HTMLParser: HTMLParser, date_suivi_copro: str, last_check_suivi_copro: str
) -> list[Any]:
    """
    Extrait les informations de situation des copropriétaires à partir d'un document HTML.

    La fonction recherche une table spécifique dans le document HTML, extrait les en-têtes et les données des lignes,
    puis nettoie et convertit les données pour les renvoyer sous forme de liste de tuples.

    Parameters:
    - HTMLParser (HTMLParser): Un objet HTMLParser contenant le document HTML à analyser.
    - date_suivi_copro (str): Une chaîne de caractères représentant la date au format JJ/MM/AAAA.
    - last_check_suivi_copro (str): Une chaîne de caractères représentant la date de dernière vérification au format JJ/MM/AAAA.

    Returns:
    - list[Any]: Une liste de tuples contenant les données des copropriétaires.
      Chaque tuple a le format suivant : (code, coproprietaire, debit, credit, date).
    """
    # Trouver la table dans le document HTML
    table = parser.css_first("table#ctzA1")

    if table:
        # Extraire les en-têtes du tableau
        headers = [
            header.text(strip=True)
            for header in table.css("td.ttA3, td.ttA4, td.ttA5, td.ttA6")
        ]
        print(f"En-têtes extraites : {headers}")  # Debug : Vérifier les en-têtes

        # Vérifier que les en-têtes nécessaires sont présents
        required_headers = ["Code", "Copropriétaire", "Débit", "Crédit"]
        header_indices = {}
        try:
            for header in required_headers:
                if header in headers:
                    header_indices[header] = headers.index(header)
                else:
                    raise ValueError(f"En-tête manquant : {header}")
        except ValueError as e:
            print(f"Erreur : {e}")
            exit(1)

        print(
            f"Indices des en-têtes : {header_indices}"
        )  # Debug : Vérifier les indices des colonnes

        # Extraire les données des lignes du tableau
        data = []
        rows = table.css("tr")[
            3:
        ]  # Ignorer les deux premières lignes (en-têtes et première ligne inutile)
        for row in rows:
            cells = [cell.text(strip=True) for cell in row.css("td")]
            print(
                f"Ligne extraite : {cells}"
            )  # Debug : Vérifier les cellules extraites
            if len(cells) >= len(
                headers
            ):  # Vérifier que la ligne contient suffisamment de colonnes
                try:
                    # Vérifier que toutes les colonnes nécessaires sont présentes
                    code = cells[header_indices["Code"]]
                    coproprietaire = cells[header_indices["Copropriétaire"]]
                    debit_str = re.findall(
                        r"[0-9]+,[0-9]{2}",
                        re.sub(r"\xa0", "", cells[header_indices["Débit"]]),
                    )
                    credit_str = re.findall(
                        r"[0-9]+,[0-9]{2}",
                        re.sub(r"\xa0", "", cells[header_indices["Crédit"]]),
                    )

                    # Vérifier si les colonnes Débit et Crédit contiennent des valeurs valides
                    debit = float(debit_str[0].replace(",", ".")) if debit_str else 0.0
                    credit = (
                        float(credit_str[0].replace(",", ".")) if credit_str else 0.0
                    )

                    # Ajouter les données nettoyées et converties à la liste
                    data.append(
                        (
                            code,
                            coproprietaire,
                            debit,
                            credit,
                            date_suivi_copro,
                            last_check_suivi_copro,
                        )
                    )
                except (IndexError, ValueError) as e:
                    print(f"Erreur : {e}. Ligne mal formatée ou données invalides.")
                    continue
            else:
                print(
                    "Erreur : Ligne mal formatée, certaines colonnes sont manquantes."
                )
    else:
        print("Tableau introuvable dans le document HTML.")
    return data


def afficher_etat_coproprietaire(data: list[Any], date_suivi_copro: str) -> None:
    """
    Affiche les informations de situation des copropriétaires dans un tableau formaté.

    La fonction prend une liste de données et une date en entrée,
    crée un tableau avec les informations des copropriétaires,
    puis affiche le tableau dans la console.

    Parameters:
    - data (list[Any]): Une liste de tuples contenant les données des copropriétaires.
      Chaque tuple doit avoir le format suivant : (code, coproprietaire, debit, credit, date).
    - date_suivi_copro (str): Une chaîne de caractères représentant la date au format JJ/MM/AAAA.

    Returns:
    - None
    """
    # Création du tableau avec les en-têtes
    table_copro = Table(title=f"Suivi des Copropriétaires au : {date_suivi_copro}")
    table_copro.add_column("Code", style="cyan", justify="center")
    table_copro.add_column("Copropriétaire", style="magenta", justify="center")
    table_copro.add_column("Débit", style="red", justify="right")
    table_copro.add_column("Crédit", style="green", justify="right")

    # Ajout des lignes de données au tableau
    for (
        code,
        coproprietaire,
        debit,
        credit,
        date_suivi_copro,
        last_check_suivi_copro,
    ) in data[2:]:
        table_copro.add_row(
            str(code),
            str(coproprietaire),
            str(debit),
            str(credit),
        )

    # Affichage du tableau dans la console
    console.print(table_copro)


def enregistrer_donnees_sqlite(data: list[Any], db_path: str) -> None:
    """
    Enregistre les données extraites dans une base de données SQLite.

    La fonction se connecte à la base de données SQLite spécifiée par `db_path`,
    crée une table "coproprietaires" si elle n'existe pas, et insère les données
    fournies dans la table.

    Parameters:
    - data (list[Any]): Une liste de tuples contenant les données à enregistrer.
      Chaque tuple doit avoir le format suivant : (code, coproprietaire, debit, credit, date).
    - db_path (str): Le chemin vers la base de données SQLite.

    Returns:
    - None
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # Création de la table si elle n'existe pas
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS coproprietaires (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            coproprietaire TEXT,
            debit REAL,
            credit REAL,
            date DATE,
            last_check DATE
        )
        """
    )
    # Insertion des données
    cur.executemany(
        "INSERT INTO coproprietaires (code, coproprietaire, debit, credit, date, last_check) VALUES (?, ?, ?, ?, ?,?)",
        data[2:],
    )
    conn.commit()
    conn.close()


date_suivi_copro, last_check_suivi_copro = recuperer_date_situation_copro(parser)
data = recuperer_situation_copro(parser, date_suivi_copro, last_check_suivi_copro)

afficher_etat_coproprietaire(data, date_suivi_copro)
# Enregistrer dans la base sqlite
enregistrer_donnees_sqlite(data, db_path)
print("Données enregistrées dans la base de données SQLite.")
# Enregistrer dans la base sqlite
# Afficher le nombre de lignes extraites
print(f"Nombre de lignes extraites : {len(data)}")
