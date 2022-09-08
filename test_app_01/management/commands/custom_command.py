"""
python manage.py custom_command all
"""
from django.core.management.base import BaseCommand, CommandError
from test_app_01.models import Patient, Visit


class Command(BaseCommand):
    help = 'Custom command to access the Django ORM'

    def add_arguments(self, parser):
        parser.add_argument('patient_ids', nargs='+', type=str)

    def handle(self, *args, **options):

        for patient_id in options['patient_ids']:
            if patient_id == 'all':
                continue
            print("Display one patient and their corresponding visits...")
            try:
                p = Patient.objects.get(patient_id=patient_id)
                visits = Visit.objects.filter(patient_id=patient_id)
            except Exception:
                raise CommandError('Error: get objects failed')
            print(f"patient_id: {p.patient_id} first_name: {p.first_name}\tdob: {p.dob}")
            for index, v in enumerate(visits):
                print(f"order: {index} id: {v.id} patient_id: {v.patient_id} visit_date: {v.visit_date}")

        # List all patients and visits
        if 'all' in options['patient_ids']:
            try:
                patients = Patient.objects.all()
                visits = Visit.objects.all()
            except Exception:
                raise CommandError('Error: get all objects failed')

            print("List all patients...")
            for index, p in enumerate(patients):
                print(f"patient: {index} patient_id: {p.patient_id} first_name: {p.first_name}\tdob: {p.dob}")

            print("List all orders...")
            for index, v in enumerate(visits):
                try:
                    print(f"order: {index} id: {v.id} patient_id: {v.patient_id} visit_date: {v.visit_date}")
                except Exception:
                    continue

        self.stdout.write(self.style.SUCCESS('Success: finished'))
