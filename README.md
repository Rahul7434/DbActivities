# Postgresql_Automate_Daily_monthly_Activities_With_Python_Django
## Structure
- **DbActivities**
  - **DbActivities**
      init.py
      asgi.py
      settings.py
      urls.py
      wsgi.py
  - **server1**
     - __pycache__
     - migrations
     - __init__.py
     - admin.py
     - apps.py
     - models.py
     - tests.py
     - views.py
  - **static**
      - css
          - bpt_mis.css
          - bot.css
      - img
          - b3.jpg
          - bg2.jpg
          - blogo.png
          - images.png
      - js
          - bot.js
          - jquery.js
  - **templates**
      - user_access.html
      - optios.html
      - index.hhtml
      - db_size.html
  - manage.py
## Features
    - Database Health Checks: Regular checks on database health metrics to ensure that databases are running optimally, including monitoring for performance issues, deadlocks, and other critical health indicators
    - User Access Reviews: Automated reviews of user access rights to ensure compliance with security policies, helping to maintain data integrity and securit
    - Login Failures Monitoring: Tracking failed login attempts to identify potential security threats and unauthorized access attempts.
    - Backup Counts: Monitoring and reporting on backup frequency and success rates to ensure that backup protocols are being followed and data recovery options are available.
    - pg_stat_activity Insights: Displaying real-time statistics of current database activity using the pg_stat_activity view, helping administrators to identify long-running queries and other performan bottlenecks.
    - Active Session Count: Providing insights into the number of active sessions to manage resource allocation and detect unusual patterns in database usage.
    - Database Sizes: Offering detailed information on the size of databases, allowing administrators to manage disk space effectively and plan for future growth.

     // We can Add more Features //
## Installation
- **Update Your System (make sure your system packages are up to date:)**
    ```
      sudo dnf update
    ```
- **Install Python and pip (CentOS 9 should come with Python 3 pre-installed, but you can install it and pip)**
    ```
        sudo dnf install python3 python3-pip
    ```
- **Install Django**
    ```
        pip install django
    ```
- **Set Up a Virtual Environment (Optional but Recommended)**
    ```
        # Install the virtualenv package if not already installed
        pip3 install virtualenv
      
        # Create a new virtual environment
        virtualenv python_Env
      
        # Activate the virtual environment
        source python_Env/bin/activate
    ```
- **Install Required Packages for the Project (Make sure to install any additional packages you need for your project. Forexample,if you're using PostgreSQL, install psycopg2.)**
    ```
       pip install psycopg2
    ```
## Set Up Django Project
        django-admin startproject DbActivities 
        cd myproject
## Start The App & add Into the settings.py file. 
      python manage.py startapp server1

      INSTALLED_APPS = [
      .......,
      'server1',
      ]

## Create Folder "Templates" & "static" to store html files and images ,css, js files in Project name dir not in Actual project folder see in stracture.
    mkdir templates
          cd templates
              html..files
    mkdir static
          cd static
              mkdir img   --to contain images .jpg, .png etc
              mkdir css   --to contain cdd files .js
              mkdir js    --to contain javascript files .js
## Add templates & static In Setting.py
  - **it points to a templates directory at the root of your project**
  - **The location where Django will collect static files**
  ```
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# TEMPLATES configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add your template directory here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```
  # Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL prefix for static files

# The location where Django will collect static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Add your static files directory here
]

## For example, static/css/style.css, it will be accessible at http://127.0.0.1:8000/static/css/style.css
```

## Create and Apply makeMigrations & Migrate.
  ```
      python manage.py makemigrations
      python manage.py migrate
  ```
## Run The Server.
  ```
  python manage.py runserver
  ```
## Access Your Application Open your web browser and go to 
  ```
      http://127.0.0.1:8000/.
  ```

## You will See First Interface of Portal. 
    - **Host Ip list**
    ```
        After Click on Host Ip will establish connecton on postgresql server & it will list out
        All Activities IN Button's Format even connection related info if fails will show error msg.
    ```

![home](https://github.com/user-attachments/assets/7c245b34-5b49-4c2d-ade2-814ad8c99a7e)

## After Click on the host it will look likes
![options](https://github.com/user-attachments/assets/dd319a3d-a980-4e5d-a775-b87de52ac407)

## If You click on any options lets say if you click on Db_sizes It will show the result on the same page with Download options. 
![db_size](https://github.com/user-attachments/assets/1096433b-7216-4de3-b7c2-07e44565eb9a)


## All activities you will see on same page with Responsive Interface.






      
