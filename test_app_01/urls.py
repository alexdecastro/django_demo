from django.urls import path
from . import views

urlpatterns = [
    path('test_page/', views.test_page, name='test_page'),
    path('test_template/', views.test_template, name='test_template'),
    path('table_template/', views.table_template, name='table_template'),
]
