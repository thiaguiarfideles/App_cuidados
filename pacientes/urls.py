from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.cadastrar_paciente_view, name='pacientes'),
]