from django import forms
from .models import *
# import GeeksModel from models.py 
  
# create a ModelForm 
class DadosPacienteForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta:
        model = DadosPaciente
        fields = ['nome', 'medico', 'email', 'cidade', 'convenios', 'hospital', 'comentarios', 'sinal_febre', 'glicemia', 'frequencia_cardiaca', 'cid', 'peso', 'altura', 'medicamento', 'horarios_medicacao']