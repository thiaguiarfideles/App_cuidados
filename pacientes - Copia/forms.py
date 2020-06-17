from django import forms
from .models import *
from crispy_forms.layout import Submit, Layout, Div, Fieldset
  
# create a ModelForm 
class DadosPacienteForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta:
        model = DadosPaciente
        fields = ['nome', 'medico', 'email', 'cidade', 'convenios', 'hospital', 'comentarios', 'sinal_febre', 'glicemia', 'frequencia_cardiaca', 'cid', 'peso', 'altura', 'medicamento', 'horarios_medicacao', 'idade', 'sexo', 'precaucao', 'banho_leito', 'Braden', 'user', 'alergia']
