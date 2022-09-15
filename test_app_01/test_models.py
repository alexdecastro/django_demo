from django.test import TestCase
import datetime
from test_app_01.models import Patient, Visit


# Create a test patient
class PatientTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(patient_id="9001", first_name="Alice Test", dob="1950-01-01", value1=20)

    def test_patient_get(self):
        test_patient = Patient.objects.get(patient_id="9001")
        self.assertEqual(test_patient.first_name, "Alice Test")
        self.assertEqual(test_patient.dob, datetime.date(1950, 1, 1))
        self.assertEqual(test_patient.value1, 20)


# Create a test visit
class VisitTestCase(TestCase):
    def setUp(self):
        test_patient = Patient.objects.create(patient_id="9001", first_name="Alice Test", dob="1950-01-01", value1=20)
        Visit.objects.create(patient_id=test_patient, visit_date="2022-08-01", result1=11, result2=51)

    def test_visit_get(self):
        test_visit = Visit.objects.get(patient_id="9001")
        self.assertEqual(test_visit.visit_date, datetime.date(2022, 8, 1))
        self.assertEqual(test_visit.result1, 11)
        self.assertEqual(test_visit.result2, 51)
