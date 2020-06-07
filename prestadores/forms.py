from django.forms import ModelForm
from django import forms

from .models import PrestadorPessoaFisica, Especialidade

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.urls import reverse


from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)

class PrestadorPessoaFisicaForm(ModelForm):
    # Uni-form
    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # helper.layout = Layout(
    #     FormActions(
    #         Submit('save_changes', 'Save changes', css_class="btn-primary"),
    #         Submit('cancel', 'Cancel'),
    #     )
    # )
    def __init__(self, *args, **kwargs):
        super(PrestadorPessoaFisicaForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-prestador-data-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_class = 'form-horizontal'
        self.fields['sn_cuidador'].label = "É Cuidador?"
        
        # self.fields["especialidades"].widget = forms.widgets.CheckboxSelectMultiple()
        self.helper.layout = Layout(
            Div(
                Div(Field('sn_cuidador',), css_class="col-md-3", ),
                Div(Field('nm_prestador'), css_class="col-md-5", ),
                Div(Field('dt_nascimento'), css_class="col-md-3", ),
                Div(Field('nr_cpf_cgc'), css_class="col-md-4", ),
                css_class="row",),
            Div(
                Div(Field('ds_codigo_conselho'), css_class="col-md-2", ),
                Div(Field('especialidades'), css_class="col-md-3", ),
                css_class="row",), 
            Div(
                Div(Field('hospital_referencia'), css_class="col-md-3", ),
                css_class="row",), 
            Div(
                Div(Field('nr_cep'), css_class="col-md-2", ),
                Div(Field('ds_endereco'), css_class="col-md-8", ),
                Div(Field('ds_complemento'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
                Div(Field('ds_bairro'), css_class="col-md-3", ),
                Div(Field('nm_cidade'), css_class="col-md-4", ),
                Div(Field('cd_uf'), css_class="col-md-2", ),
                Div(Field('nr_fone_contato'), css_class="col-md-3", ),
                Div(Field('ds_email'), css_class="col-md-3", ),
                css_class="row", ),
            Div(
                Div(Field('identidade_frente',css_class="filestyle",data_input="false",data_buttonText="Upload"), css_class="col-md-3", ),
                Div(Field('identidade_verso',css_class="filestyle",data_input="false",data_buttonText="Upload"), css_class="col-md-3", ),
                Div(Field('comprovante_residencia',css_class="filestyle",data_input="false",data_buttonText="Upload"), css_class="col-md-3", ),
            css_class="row", ),
            Div(
                Div(Field('observacoes'), css_class="col-md-12 col-centered", ),
                css_class="row", ),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = PrestadorPessoaFisica
        # fields = ['sn_cirurgiao', 'nm_prestador', 'nr_cpf_cgc', 'dt_nascimento', 'nm_mae', 'nm_pai',
        #           'ds_codigo_conselho', 'especialidades',
        #           'ds_faculdade', 'ds_email', 'nr_cep', 'ds_endereco', 'ds_complemento', 'ds_bairro', 'nm_cidade',
        #           'cd_uf', 'banco','ds_agencia', 'nr_conta', 'nr_fone_contato', 'identidade_frente', 'identidade_verso',
        #           'comprovante_residencia',
        #           'observacoes']
        fields = ['sn_cuidador', 'nm_prestador', 'nr_cpf_cgc', 'dt_nascimento', 
                  'ds_codigo_conselho', 'especialidades', 'hospital_referencia',
                   'ds_email', 'nr_cep', 'ds_endereco', 'ds_complemento', 'ds_bairro', 'nm_cidade',
                  'cd_uf', 'banco','ds_agencia', 'nr_conta', 'nr_fone_contato', 'identidade_frente', 'identidade_verso',
                  'comprovante_residencia',
                  'observacoes']
        widgets = {
            'especialidades': Select2MultipleWidget
        }
        
       
        # self.helper.add_input(Submit('submit', 'Enviar', css_class='btn-success'))

        # self.helper.layout = Layout(
        #     Div('sn_cirurgiao',css_class="col-lg-4",),
        #     Div('nm_prestador'),
        #     Div('nr_cpf_cgc'),
        #     Div('dt_nascimento'),
        #     #
        #     # Fieldset('Dados Pessoais',
        #     #          Field('nm_tip_presta', placeholder='Tipo de Prestador',
        #     #                css_class="some-class"),
        #     #          Div('sn_cirurgiao', title="Cirurgião?"), ),
        #     # Fieldset('Contact data', 'nm_prestador', 'nr_cpf_cgc', style="color: brown;"),
        #     # InlineRadios('color'),
        #     # TabHolder(Tab('Address', 'address'),
        #     #           Tab('More Info', 'more_info'))
        # )



        # # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'Enviar'))


#
# class NewPrestadorForm(forms.Form):
#     name = forms.CharField(
#         max_length=255,
#         widget=forms.Textarea(
#             attrs={'class': 'custom'},
#         ),
#     )


class DadosPessoaisForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DadosPessoaisForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-dados-pessoais-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div(Field('nm_prestador'), css_class="col-md-6", ),
                Div(Field('nr_cpf_cgc'), css_class="col-md-4", ),
                Div(Field('dt_nascimento'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
                Div(Field('nm_mae'), css_class="col-md-6", ),
                Div(Field('nm_pai'), css_class="col-md-6", ),
                css_class="row", ),
            Div(
                Div(Field('nr_cep'), css_class="col-md-2", ),
                Div(Field('ds_endereco'), css_class="col-md-8", ),
                Div(Field('ds_complemento'), css_class="col-md-2", ),
                css_class="row", ),
            Div(
                Div(Field('ds_bairro'), css_class="col-md-3", ),
                Div(Field('nm_cidade'), css_class="col-md-4", ),
                Div(Field('cd_uf'), css_class="col-md-2", ),
                css_class="row", ),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = PrestadorPessoaFisica
        fields = ['nm_prestador','nr_cpf_cgc','dt_nascimento','nm_mae','nm_pai',
                  'nr_cep','ds_endereco','ds_complemento','ds_bairro','nm_cidade','cd_uf','observacoes']
        exclude=['usuario']
        widgets= {
            'especialidades': Select2MultipleWidget,
            
        }