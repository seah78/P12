# CRM

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

### Pré-requis

- Python 3.9 (Installer Python 3.9 depuis https://www.python.org/)
- PostgreSQL (Installer PostgreSQL depuis https://www.postgresql.org/)
- Terminal
- Git
- Postman
- Navigateur


### Installation et exécution de l'application sans pipenv (avec venv et pip)

1. Clonez ce dépôt de code à l'aide de la commande `git clone https://github.com/seah78/P12.git`
2. Rendez-vous depuis un terminal dans le répertoire avec la commande `cd P12`
3. Créer un environnement virtuel pour le projet avec `python -m venv env` sous windows ou `python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `env\Scripts\activate` sous windows ou `source env/bin/activate` sous macos ou linux.
5. Installez les dépendances du projet avec la commande `pip install -r requirements.txt`
6. Créer une base de donnée PostgreSQL (Documentation : https://docs.postgresql.fr/14/)
7. Configurer le fichier `settings.py` avec les paramètres d'accès à la base de donnée
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nom_bdd',
            'USER': 'user_bdd',
            'PASSWORD': 'password_bdd',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    
8. Migrer les modèles vers la base de données avec la commande `python manage.py migrate`
9. Créer un superuser avec la commande avec la commande `python manage.py createsuperuser`
10. Démarrer le serveur avec `python manage.py runserver`

Les étapes 1 à 9 ne sont requises que pout l'installation initiale. Pour les lancements ultérieurs du serveur, il suffit d'exécuter l'étapes 10 à partir du répertoire P12.


## Documentation de l'API

La documentation de l'API est accessible à cette adresse : https://documenter.getpostman.com/view/19380541/UVyvwEcr

## Démarrage de l'API

Depuis un navigateur ou depuis Postman saisissez l'adresse http://127.0.0.1:8000/


## Fabriqué avec

* Visual Studio Code

## Versions

Version actuelle : v1.0.0
Liste des versions : [Cliquer pour afficher](https://github.com/seah78/P12/tags)

## Auteurs

* ** Sébastien HERLANT ** _alias_ [@seah78](https://github.com/seah78)

## License

Ce projet est sous licence ``exemple: WTFTPL`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations


