from django.db import models
from usuarios.models import User
from geoposition.fields import GeopositionField

class localizacao(models.Model):
    name = models.CharField(verbose_name="Nome Cliente", max_length=100)
    position = GeopositionField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    dt_envio = models.DateTimeField(auto_now_add=True)
