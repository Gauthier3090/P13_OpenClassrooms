## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Prérequis

Pour configurer le déploiement, vous devez avec un compte sur les sites suivants :

- Compte GitHub
- Compte CircleCi (associé à votre compte GitHub)
- Compte Docker
- Compte Heroku
- Compte Sentry

### Résumé

Le déploiement de l'application est automatisé par le pipeline CircleCI. 
Lorsque les mises à jour sont transmises au référentiel GitHub, 
le pipeline déclenche la suite de tests et le linting de code pour toutes les branches du projet. 
Si des mises à jour sont faites sur la branche master, et si et seulement si les tests 
et linting passent, le workflow construit une image Docker et la met sur le DockerHub.
Si l'étape réussie, alors l'application se déploie sur Heroku.

### Configuration

#### CircleCI

Après avoir cloné le projet, configurez l'environnement virtuel local (voir Développement local) 
et créez les comptes requis. Configurez un nouveau projet sur CircleCI via "Configurer le projet". 
Pour terminer, sélectionnez la branche master comme source pour le fichier .circleci/config.yml.


Ensuite, mettez en place les variables d'environnements suivantes (Project settings -> Environnement Variables):

- DJANGO_SECRET_KEY → Clé du projet django
- SENTRY_DSN → Lien URL du projet Sentry
- DOCKER_LOGIN → Login de votre compte Docker
- DOCKER_PASSWORD → Mot de passe de votre compte Docker
- DOCKER_REPO → Nom du répertoire du docker
- HEROKU_APP_NAME → Nom de votre application Heroku
- HEROKU_TOKEN → Token trouvable dans Heroku API Key


#### Heroku

Pour créer une application Heroku, il y a plusieurs méthodes possibles :

Méthode 1 : Créer manuellement l'application sur le site de Heroku.
Le nom doit correspondre à la variable d'environnement HEROKU_APP_NAME. 
Installez-les addons Heroku Postgres.

Méthode 2 : Installer le HEROKU CLI.
Utilise la commande heroku ```apps:create <app-name> --region eu --addons=heroku-postgresql```
avec le nom de votre application. Le nom doit correspondre à la variable d'environnement HEROKU_APP_NAME.

Méthode 3 : Configurez le pipeline avec le fichier CircleCi et ajouter ces lignes suivantes :

Créer une nouvelle application et ajoute l'addon postgres :
```HEROKU_API_KEY=${HEROKU_TOKEN} heroku apps:create $HEROKU_APP_NAME --region eu --addons=heroku-postgresql```

Installe postgres heroku sur une application existante :
```HEROKU_API_KEY=${HEROKU_TOKEN} heroku addons:create heroku-postgresql -a $HEROKU_APP_NAME --confirm $HEROKU_APP_NAME```


#### Sentry

Après avoir créé un compte Sentry, mettez en place la variable SENTRY_DSN (Project Settings -> Client Keys).

Pour tester Sentry, utilisez la terminaison sentry qui effectuera une division par 0 et
il créera un rapport d'erreur sur Sentry. 
