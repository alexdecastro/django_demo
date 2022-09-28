from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Patient, Visit

import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go


# Return a JsonResponse
def test_json_response(request):
    response = {
        'ok': True,
        'message': 'This is a message.',
    }
    return JsonResponse(response)


# Return a HttpResponse
def test_page(request):
    return HttpResponse('<h1>Test Page</h1>')


# Render a template
def test_template(request):
    return render(request, 'app/test_template.html', {'title': 'Test Template'})


# Render a table view
def table_template(request):
    patients = Patient.objects.all()
    visits = Visit.objects.all()

    context = {
        'title': 'Patients',
        'patients': patients,
        'visits': visits,
    }
    return render(request, 'app/table_template.html', context)


# Render a barchart view
def barchart_view(request):
    def plot_div1():
        df = pd.DataFrame(
            {
                "patient_id": ["0001", "0002", "0003", "0004"],
                "first_name": ["Alice", "Bob", "Carol", "David"],
                "dob": ["1950-01-01", "1950-02-02", "1950-03-03", "1950-04-04"],
                "value1": [20, 30, 40, 50],
                "value2": [10, 2, 8, 4],
            }
        )
        fig = px.bar(df, x="first_name", y="value1", color="value1", barmode="group")
        fig.update_layout(barmode='stack')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def plot_div2():
        patients = Patient.objects.all().order_by('first_name')
        names = [p.first_name for p in patients]
        values = [p.value1 for p in patients]

        trace = [
            go.Bar(name='values', x=names, y=values),
        ]
        layout = dict(
            title='Barchart'
        )
        fig = go.Figure(data=trace, layout=layout)
        fig.update_layout(barmode='stack')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'title': 'Barchart',
        'plot1': plot_div1(),
        'plot2': plot_div2(),
    }

    return render(request, 'app/barchart.html', context)
