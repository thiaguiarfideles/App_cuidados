from django.contrib import admin

from pacientes.models import DadosPaciente, Medicamentos, Farm_medicamentos, Nome_paciente, Medico

admin.site.register(DadosPaciente)
admin.site.register(Medicamentos)
admin.site.register(Farm_medicamentos)
admin.site.register(Nome_paciente)
admin.site.register(Medico)