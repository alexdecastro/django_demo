from django.urls import path
from . import views

urlpatterns = [
    path('test_json_response/', views.test_json_response, name='test_json_response'),
    path('test_page/', views.test_page, name='test_page'),
    path('test_template/', views.test_template, name='test_template'),
    path('table_template/', views.table_template, name='table_template'),
    path('barchart/', views.barchart_view, name='barchart_view'),
]
