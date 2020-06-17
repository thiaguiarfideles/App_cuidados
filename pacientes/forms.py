from django.forms import ModelForm
from django import forms

from pacientes.models import DadosPaciente

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions




class DadosPacienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DadosPacienteForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-dados-paciente-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_tag = False
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome'), css_class="col-md-5", ),
                Div(Field('medico'), css_class="col-md-5", ),
                css_class="row", ),
            Div(
                Div(Field('convenios'), css_class="col-md-5", ),
                Div(Field('hospital'), css_class="col-md-5", ),
                css_class="row", ),
            Div(
            	Div(Field('cidade'), css_class="col-md-3", ),
            	Div(Field('email'), css_class="col-md-3", ),
            	css_class="row", ),
            Div(
            	Div(Field('idade'), css_class="col-md-2", ),
                Div(Field('sexo'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
                
                Div(Field('sinal_febre'), css_class="col-md-2", ),
                Div(Field('glicemia'), css_class="col-md-2", ),
                Div(Field('frequencia_cardiaca'), css_class="col-md-2", ),
                Div(Field('cid'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
                Div(Field('peso'), css_class="col-md-2", ),
                Div(Field('altura'), css_class="col-md-2", ),
                Div(Field('nm_medicamento'), css_class="col-md-2", ),
                Div(Field('horarios_medicacao'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
                Div(Field('precaucao'), css_class="col-md-2", ),
                Div(Field('banho_leito'), css_class="col-md-2", ),
                Div(Field('Braden'), css_class="col-md-2", ),
                Div(Field('alergia'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
            	Div(Field('user'), css_class="col-md-2", ),
            	css_class="row", ),
            Div(
                Div(Field('comentarios'), css_class="col-md-8", ),



                css_class="row", ),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = DadosPaciente
        fields = ['nome', 'medico', 'email', 'cidade', 'convenios', 'hospital', 'comentarios', 'sinal_febre', 'glicemia', 'frequencia_cardiaca',
         'cid', 'peso', 'altura', 'nm_medicamento', 'horarios_medicacao', 
         'idade', 'sexo', 'precaucao', 'banho_leito', 'Braden', 'alergia', 'user']
        