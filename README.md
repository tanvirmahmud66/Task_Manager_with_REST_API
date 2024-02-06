1) Download and install Git form online.

   
3) clone the project-
   -> git clone https://github.com/tanvirmahmud66/Task_Manager_with_REST_API.git

4) Download and install python from online.

5) navigate project directory
    -> cd Task_Manager_with_REST_API

6) create virtual environment
    -> python -m venv venv

7) active virtual environment
    -> source venv/bin/activate (macOS)
    -> venv/bin/activate (windows)

8) Install Project Dependencies
    -> pip install -r requirements.txt

9) before database migrations go to project root folder tasks_manager and then settings.py and find database configuration
    -> if postgreSQL installed in your machine then just change the database name, and then create .env with DB_USER for your root username of postgreSQL and DB_PASSWORD for your root db password
    -> if postgreSQL not installed in your machine then comment the database config setting and uncomment the upper config of database that commented out for SQLite3 Default database

10) Database Migration (go to the directory have manage.py) 
    -> python manage.py makemigrations
    (and then)
    -> python manage.py migrate

11) Before run the main application createsuper user for admin
    -> python3 manage.py createsuperuser
    (give all the requirement that ask for)

12) Run the Application
    -> Python manage.py runserver


   

