from django.db import models


class Patient(models.Model):
    patient_id = models.CharField(db_column='patient_id', max_length=32, primary_key=True)
    first_name = models.CharField(db_column='first_name', max_length=32, blank=True, null=True)
    dob = models.DateField(db_column='dob', blank=True, null=True)
    value1 = models.IntegerField(db_column='value1', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_id', blank=True, null=True)
    visit_date = models.DateField(db_column='visit_date', blank=True, null=True)
    result1 = models.IntegerField(db_column='result1', blank=True, null=True)
    result2 = models.IntegerField(db_column='result2', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit'
