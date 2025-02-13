# Projet Django : Formulaire de Connexion et d'Inscription Sécurisé

## Description du Projet

Ce projet Django, qui s'appelle **django-formulaire**, a pour objectif de créer un formulaire de connexion et d'inscription sécurisé. Le projet est conçu pour être exécuté en local uniquement. Il met en œuvre plusieurs mesures de sécurité pour protéger les données des utilisateurs et prévenir les attaques courantes.

## Structure du Projet

Le projet est structuré comme suit :

```plaintext 
django-formulaire/
│
├── application/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── validators.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   └── application/
│   │       ├── logo_dragon.jpg
│   │       └── style.css
│   ├── templates/
│   │   └── application/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       └── registration.html
│   └── __pycache__/
│
├── formulaire/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── .env.example
│   └── __pycache__/
│
├── staticfiles/
│   └── admin/
│       ├── css/
│       ├── img/
│       └── js/
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```


## Installation et Configuration

### Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)

### Étapes pour lancer le projet

1. **Cloner le dépôt GitHub** :

   ```bash
   git clone https://github.com/DaSilvaThomas/django-formulaire.git
   ```
   ```bash
   cd django-formulaire
   ```

2. **Créer un environnement virtuel** :

    ```bash
    python -m venv env
    ```

3. **Activer l'environnement virtuel** :

- Sur Windows :
    ```bash
    env\Scripts\activate
    ```

- Sur macOS/Linux :
    ```bash
    source env/bin/activate
    ```

4. **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

5. **Renommez le fichier .env.example en .env** :

   ```bash
   cd formulaire
   ```

- Sur Windows :
   ```bash
   ren ".env.example" ".env"
   ```

- Sur macOS/Linux :
   ```bash
   mv formulaire/.env.example formulaire/.env
   ```

6. **Ouvrez le fichier .env et remplissez les valeurs manquantes** :

   **SECRET_KEY** :
   La clé secrète Django est utilisée pour sécuriser les sessions et les données sensibles. Vous devez générer une clé sécurisée et unique. Exemple de clé :
   ```plaintext
   SECRET_KEY='django-insecure-votre_clé_secrète_ici_1234567890!@#$%^&*'
   ```
   - Vous pouvez générer une clé sécurisée sur ce site : https://djecrety.ir/

   **ADMIN_URL** :
   L'URL d'administration est utilisée pour accéder à l'interface d'administration de Django. Pour des raisons de sécurité, il est recommandé de ne pas utiliser l'URL par défaut (admin/). Ajoutez des chiffres ou des caractères aléatoires pour la rendre plus difficile à deviner. Exemple :
   ```plaintext
   ADMIN_URL='admin-arc45y6/'
   ```
   - Remarque : N'oubliez pas le **/** à la fin de l'URL.

8. **Configurer la base de données** :

    Le projet utilise SQLite par défaut. Vous pouvez exécuter les migrations pour créer la base de données (se placer à la racine du projet) :
    ```bash
    python manage.py migrate
    ```
    
10. **(Optionnel) Créer un compte superutilisateur** :

   Si vous souhaitez accéder à l'interface d'administration Django, vous pouvez créer un compte superutilisateur en ligne de commande :
   ```bash
   python manage.py createsuperuser
   ```

11. **Lancer le serveur de développement** :

    ```bash
    python manage.py runserver
    ```

12. **Accéder à l'application** :

    Ouvrez votre navigateur et accédez à http://localhost:8000/login/ pour la page de connexion.


## Mesures de Sécurité

1. **Désactivation du mode Debug** :

    Dans settings.py, le mode DEBUG est désactivé (DEBUG = False) pour éviter l'exposition d'informations sensibles en production.

2. **Protection CSRF** :

    Django inclut une protection CSRF par défaut. Le middleware CsrfViewMiddleware est activé dans settings.py pour protéger contre les attaques de type Cross-Site Request Forgery.

3. **Validation des mots de passe** :

    Le projet utilise un validateur personnalisé PasswordComplexityValidator pour s'assurer que les mots de passe respectent les critères suivants :

    - Au moins 12 caractères
    - Au moins une lettre majuscule
    - Au moins une lettre minuscule
    - Au moins un chiffre
    - Au moins un caractère spécial

    Ce validateur est ajouté dans settings.py sous AUTH_PASSWORD_VALIDATORS.

4. **Cookies HTTPOnly** :

    Le paramètre SESSION_COOKIE_HTTPONLY est activé dans settings.py pour empêcher l'accès aux cookies de session via JavaScript, réduisant ainsi le risque de vol de session via des scripts malveillants.

5. **Utilisation de WhiteNoise** :

    Le middleware WhiteNoise est utilisé pour servir les fichiers statiques de manière sécurisée en production.

6. **Connexion et Déconnexion Sécurisées** :

    Les vues de connexion et de déconnexion utilisent les fonctions intégrées de Django (authenticate, login, logout) pour gérer les sessions de manière sécurisée.

    La vue login_view vérifie si l'utilisateur est déjà connecté avant de tenter une nouvelle connexion, évitant ainsi les redondances.

7. **Protection contre les attaques par clic** :

    Le middleware XFrameOptionsMiddleware est activé pour empêcher les attaques de type "clickjacking" en définissant l'en-tête HTTP X-Frame-Options.


## Nouvelles Mesures de Sécurité Ajoutées

1. **OWASP A1** : Injections SQL et attaques XSS
    
    Protection contre les injections SQL :

    - Django utilise un ORM (Object-Relational Mapping) qui prévient les injections SQL en échappant automatiquement les entrées utilisateur.

    Protection contre les attaques XSS :

    - Le paramètre SECURE_BROWSER_XSS_FILTER est activé dans settings.py pour activer le filtre XSS côté navigateur. De plus, Django échappe automatiquement les données dans les templates pour prévenir les attaques XSS.

2. **OWASP A3** : Exposition de données sensibles

    Utilisation de django-environ pour la gestion des variables sensibles :

    - Les variables sensibles telles que SECRET_KEY, DEBUG, et ALLOWED_HOSTS sont désormais stockées dans un fichier .env situé dans le dossier formulaire/. Ce fichier est ignoré par Git pour éviter l'exposition accidentelle de ces informations sensibles.

3. **OWASP A5** : Mauvaise gestion des accès

    Validation des noms d'utilisateurs :

    - Le formulaire de connexion et d'inscription utilise une classe SafeCharField pour valider les noms d'utilisateurs. Cette classe empêche l'utilisation de caractères spéciaux non autorisés, réduisant ainsi le risque d'injection de code malveillant.

    Redirection sécurisée après connexion/déconnexion :

    - Les vues de connexion et de déconnexion redirigent les utilisateurs vers des pages sécurisées (home ou login) après chaque action, évitant ainsi les redirections non contrôlées.

4. **OWASP A8** : Falsification de requête côté serveur (SSRF)

    Absence de vulnérabilité SSRF :

    - Le projet ne traite pas d'URLs fournies par l'utilisateur et ne contient aucune fonctionnalité qui envoie des requêtes HTTP vers des URLs externes. Par conséquent, il n'est pas vulnérable aux attaques de type SSRF (Server-Side Request Forgery).


## Fichiers Importants

- settings.py : Contient les configurations du projet, y compris les paramètres de sécurité.
- views.py : Contient les vues pour la connexion, la déconnexion, l'inscription et la page d'accueil.
- forms.py : Définit les formulaires de connexion et d'inscription.
- validators.py : Contient le validateur personnalisé pour la complexité des mots de passe.
- templates/ : Contient les templates HTML pour les pages de connexion, d'inscription et d'accueil.
- static/ : Contient les fichiers static du projet.
- .env : Fichier de configuration des variables d'environnement, situé dans le dossier formulaire/
