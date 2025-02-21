from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('add-patient/', views.add_patient, name='add_patient'),
]
