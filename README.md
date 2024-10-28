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

    ![image](https://github.com/user-attachments/assets/5413e5d5-d845-4dfd-89a3-21d534e89314)

## Add app into App DICT In Settings.py file.



      
