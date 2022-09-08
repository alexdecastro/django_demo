from django.shortcuts import render
from django.http import HttpResponse

from test_app_01.models import Patient, Visit


# Create your views here.
def test_page(request):
    return HttpResponse('<h1>test_app_01 Test Page</h1>')


def test_template(request):
    patient = Patient.objects.get(patient_id='0001')
    print("patient_id: ", patient.patient_id)
    print("first_name: ", patient.first_name)
    print("dob: ", patient.dob)
    print("value1: ", patient.value1)

    visit = Visit.objects.get(patient_id='0001')
    print("id: ", visit.id)
    print("patient_id: ", visit.patient_id)
    print("visit_date: ", visit.visit_date)
    print("result1: ", visit.result1)
    print("result2: ", visit.result2)

    return render(request, 'test_app_01/test_template.html', {'title': 'Test Template'})


def table_template(request):
    patients = Patient.objects.all()
    visits = Visit.objects.all()

    context = {
        'title': 'Patients',
        'patients': patients,
        'visits': visits,
    }
    return render(request, 'test_app_01/table_template.html', context)
