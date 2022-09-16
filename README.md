## Django demo for tracking patients and visits

A Django demo for loading patients and visits from a SQL database using the Django ORM. This demo uses data tables, barcharts and unit tests.

### Data Tables
Patients and visits are displayed in data tables.
![Table of patients and visits](images/screenshot-01.png)

### Barcharts
Barcharts created with plotly.
![Barcharts created with plotly](images/screenshot-02.png)

### Unit Tests
Run unit tests for models.
```console
python manage.py test --keepdb test_app_01.test_models
```

Run unit tests for views.
```console
python manage.py test --keepdb test_app_01.test_views
```
