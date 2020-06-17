from django.contrib import admin

from pacientes.models import DadosPaciente, Medicamentos

admin.site.register(DadosPaciente)
admin.site.register(Medicamentos)