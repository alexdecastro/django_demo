## Django demo for tracking patients and visits

A Django demo for loading patients and visits from a SQL database using the Django ORM. This demo uses data tables, barcharts and unit tests.

### Data Tables
Patients and visits are displayed in data tables.
![Table of patients and visits](images/screenshot-01.png)

### Barcharts
Barcharts created with plotly.
![Barcharts created with plotly](images/screenshot-02.png)

### Clone and run the project

Clone the repository
```console
cd <project_directory>
git clone https://github.com/alexdecastro/django_demo.git src
```

Create and activate a virtual environment
```console
python -m venv env
source env/bin/activate
```

Install required packages using requirements.txt
```console
pip install -r ./src/requirements.txt
```

Create a test database
```console
psql -p 5432 -U postgres -c 'CREATE DATABASE test_database;'
psql -p 5432 -U postgres -f test_data.sql -d test_database
```

Run the project
```console
cd src
export SECRET_KEY='secret_key'
export PGPORT=5432
python manage.py runserver
```

### Unit Tests
Run unit tests for models.
```console
python manage.py test --keepdb app.test_models
```

Run unit tests for views.
```console
python manage.py test --keepdb app.test_views
```

### Custom Commands
Run a custom command.
```console
python manage.py custom_command all
```
