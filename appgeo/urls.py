from django.urls import path
from . import views

app_name = 'appgeo'

urlpatterns = [
    path('', views.localizacao_view, name='appgeo'),
]