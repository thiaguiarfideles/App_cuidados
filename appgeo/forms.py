from django import forms
from appgeo.models import localizacao
  
# create a ModelForm 
class localizacaoForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta:
        model = localizacao
        fields = '__all__'