# Generated by Django 4.1.1 on 2022-09-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(db_column='patient_id', max_length=32, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='first_name', max_length=32, null=True)),
                ('dob', models.DateField(blank=True, db_column='dob', null=True)),
                ('value1', models.IntegerField(blank=True, db_column='value1', null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_date', models.DateField(blank=True, db_column='visit_date', null=True)),
                ('result1', models.IntegerField(blank=True, db_column='result1', null=True)),
                ('result2', models.IntegerField(blank=True, db_column='result2', null=True)),
            ],
            options={
                'db_table': 'visit',
                'managed': False,
            },
        ),
    ]
