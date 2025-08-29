---
applyTo: '**'
---
Tu es un fichier Python. Voici quelques instructions pour t'aider à écrire du code Python de haute qualité :
1. **Respecte les conventions PEP 8** : Utilise des indentations de 4 espaces, des lignes de moins de 79 caractères, et des noms de variables en snake_case.
2. **Utilise des types explicites** : Ajoute des annotations de type pour toutes les fonctions et méthodes.
3. **Gère les exceptions de manière appropriée** : Utilise des blocs try-except pour gérer les erreurs potentielles.
4. **Commentaires et documentation** : Commente ton code de manière claire et concise. Utilise des docstrings pour documenter les fonctions et les classes. 
5. **Utilise des bibliothèques standard** : Privilégie les bibliothèques standard de Python avant d'ajouter des dépendances externes.
6. **Tests unitaires** : Écris des tests unitaires pour les fonctions critiques afin d'assurer leur bon fonctionnement.
7. **Optimisation des performances** : Évite les opérations coûteuses dans les boucles et utilise des structures de données appropriées.
8. **Utilise des environnements virtuels** : Pour gérer les dépendances, utilise des environnements virtuels comme poetry.
9. **Respecte le principe DRY (Don't Repeat Yourself)** : Évite la duplication de code en créant des fonctions réutilisables.
10. **Utilise des outils de linting** : Intègre des outils comme pylint ou flake8 ou ruff dans ton flux de travail pour maintenir la qualité du code.
11. **Versionnage** : Utilise un système de contrôle de version comme Git pour suivre les modifications de ton code.
12. **Sécurité** : Sois vigilant quant à la sécurité, surtout lorsque tu manipules des données sensibles ou des entrées utilisateur.
13. **Performance** : Profile ton code pour identifier les goulots d'étranglement et optimise les parties critiques.
14. **Lisibilité** : Priorise la lisibilité du code. Un code clair est souvent plus important qu'un code astucieux.
15. **Mise à jour des dépendances** : Assure-toi que les bibliothèques externes utilisées sont à jour pour bénéficier des dernières fonctionnalités et correctifs de sécurité.
16. **Utilise des context managers** : Pour la gestion des ressources (fichiers, connexions réseau, etc.), utilise des context managers (avec l'instruction `with`) pour assurer une libération appropriée des ressources.
17. **Modularité** : Divise ton code en modules et packages pour améliorer la maintenabilité et la réutilisabilité.
18. **Utilise des f-strings** : Pour la concaténation de chaînes, utilise des f-strings (disponibles à partir de Python 3.6) pour une syntaxe plus claire et performante.
19. **Évite les variables globales** : Limitee l'utilisation des variables globales pour réduire les effets de bord et améliorer la testabilité du code.
20. **Utilise des listes en compréhension** : Pour créer des listes de manière concise et efficace, utilise des listes en compréhension au lieu de boucles for traditionnelles. 
21. **Utilise des générateurs** : Pour traiter de grandes quantités de données, utilise des générateurs pour économiser de la mémoire.
22. **Utilise des bibliothèques de gestion de configuration** : Pour gérer les configurations, utilise des bibliothèques comme `configparser` ou `pydantic` pour une gestion plus robuste et flexible.    
23. **Utilise des décorateurs** : Pour ajouter des fonctionnalités à des fonctions ou des méthodes de manière réutilisable, utilise des décorateurs.    
24. **Utilise des assertions** : Pour vérifier les conditions qui doivent toujours être vraies, utilise des assertions pour attraper les erreurs tôt dans le développement.
25. **Utilise des environnements de développement intégrés (IDE)** : Utilise des identifiers de code comme PyCharm, VSCode ou autres pour bénéficier de fonctionnalités avancées comme l'autocomplétion, le débogage et la gestion des projets.  
26. **Utilise des outils de formatage automatique** : Intègre des outils comme Black ou Autopep8 dans ton flux de travail pour maintenir un style de code cohérent.
27. **Utilise des outils de documentation** : Utilise des outils comme Sphinx pour générer la documentation de ton code de manière professionnelle.
28. **Utilise des outils d'intégration continue (CI)** : Mets en place des pipelines CI avec des outils comme GitHub Actions, Travis CI ou Jenkins pour automatiser les tests et le déploiement de ton code.
29. **Utilise des outils de gestion des dépendances** : Utilise des outils comme Poetry ou Pipenv pour gérer les dépendances de ton projet de manière efficace et reproductible.
30. **Reste informé des nouveautés Python** : Suis les évolutions du langage Python et des bibliothèques populaires pour tirer parti des nouvelles fonctionnalités et améliorations.
31. **Utilise des structures de données appropriées** : Choisis les structures de données (listes, tuples, ensembles, dictionnaires) en fonction des besoins spécifiques de ton application pour optimiser les performances et la lisibilité.
32. **Utilise des fonctions lambda et des fonctions d'ordre supérieur** : Pour des opérations simples et des transformations de données, utilise des fonctions lambda et des fonctions d'ordre supérieur comme `map()`, `filter()` et `reduce()` pour un code plus concis et expressif.
33. **Utilise des bibliothèques de manipulation de données** : Pour les projets impliquant des données, utilise des bibliothèques comme Pandas ou NumPy pour des opérations efficaces et performantes sur les ensembles de données.
34. **Utilise des outils de profiling** : Pour identifier les goulots d'étranglement dans ton code, utilise des outils de profiling comme cProfile ou line_profiler pour analyser les performances et optimiser les parties critiques.
35. **Utilise des environnements de conteneurs** : Pour assurer la portabilité et la cohérence des environnements de développement et de production, utilise des outils comme Docker pour créer des conteneurs légers et isolés.
36. **Utilise des outils de gestion de projet** : Pour organiser et suivre les tâches de développement, utilise des outils de gestion de projet comme Jira, Trello ou Asana pour améliorer la collaboration et la productivité de l'équipe.
37. **Utilise des outils de visualisation de données** : Pour représenter graphiquement les données, utilise des bibliothèques comme Matplotlib, Seaborn ou Plotly pour créer des visualisations claires et informatives.
38. **Utilise des outils de gestion des versions de données** : Pour les projets impliquant des ensembles de données volumineux, utilise des outils comme DVC (Data Version Control) pour suivre les modifications et gérer les versions des données.
39. **Utilise des outils de gestion des secrets** : Pour gérer les informations sensibles comme les clés API et les mots de passe, utilise des outils comme HashiCorp Vault ou AWS Secrets Manager pour assurer la sécurité et la confidentialité des données.
40. **Utilise des outils de surveillance et de journalisation** : Pour suivre les performances et les erreurs de ton application en production, utilise des outils comme Prometheus, Grafana ou ELK Stack pour une surveillance efficace et une journalisation centralisée.
41. **Utilise des outils de test de performance** : Pour évaluer les performances de ton application sous charge, utilise des outils comme Locust ou JMeter pour simuler des utilisateurs et identifier les points faibles.42. **Utilise des outils de gestion des dépendances de sécurité** : Pour identifier et gérer les vulnérabilités dans les dépendances de ton projet, utilise des outils comme Dependabot ou Snyk pour assurer la sécurité de ton code.
43. **Utilise des outils de gestion des configurations d'infrastructure** : Pour automatiser la gestion et le déploiement de l'infrastructure, utilise des outils comme Ansible, Terraform ou Chef pour une gestion efficace et reproductible.
44. **Utilise des outils de gestion des performances des applications (APM)** : Pour surveiller et optimiser les performances de ton application en production, utilise des outils comme New Relic, Datadog ou AppDynamics pour une visibilité approfondie et une analyse des performances.
45. **Utilise des outils de gestion des erreurs** : Pour capturer et gérer les erreurs en production, utilise des outils comme Sentry ou Rollbar pour une surveillance proactive et une résolution rapide des problèmes.
46. **Utilise des outils de gestion des API** : Pour concevoir, documenter et gérer les API de ton application, utilise des outils comme Swagger, Postman ou Apigee pour une gestion efficace et une collaboration facilitée.
47. **Utilise des outils de gestion des workflows** : Pour automatiser les processus de développement et de déploiement, utilise des outils comme Apache Airflow ou Prefect pour une orchestration efficace des tâches.
48. **Utilise des outils de gestion des dépendances de développement** : Pour gérer les dépendances spécifiques à l'environnement de développement, utilise des outils comme tox ou nox pour assurer la cohérence et la reproductibilité des environnements.
49. **Utilise des outils de gestion des versions de code** : Pour gérer les branches, les fusions et les versions de ton code, utilise des outils comme GitFlow ou GitHub Flow pour une gestion efficace et structurée du développement.
50. **Utilise le francais** : Écris tout le code, les commentaires et la documentation en français pour assurer la cohérence linguistique dans le projet.