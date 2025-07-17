import requests
from dotenv import load_dotenv
import os

load_dotenv()

login_site_copro = os.getenv("login_site_copro")
password_site_copro = os.getenv("password_site_copro")
# URL de connexion
url_site_copro = os.getenv("url_site_copro")

# Données d'authentification (remplacez par vos identifiants)
payload = {"username": login_site_copro, "password": password_site_copro}

# Créer une session pour gérer les cookies
session = requests.Session()

# Envoyer la requête POST pour s'authentifier
response = session.post(url_site_copro, data=payload)

# Vérifier si la connexion a réussi
if response.ok:
    print("Connexion réussie !")
    # Vous pouvez maintenant utiliser `session` pour accéder aux pages protégées
else:
    print("Échec de la connexion.")
