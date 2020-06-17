from registration.forms import RegistrationForm, RegistrationFormUniqueEmail
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from django.utils.html import format_html #para colocar o link na msg de erro
from django.contrib.auth import get_user_model
from .models import UserProfile
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset
UserModel = get_user_model
User = UserModel()

class MyRegForm(RegistrationFormUniqueEmail):

    def __init__(self, *args, **kwargs):
        super(MyRegForm, self).__init__(*args, **kwargs)
        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        # msg = format_html("""Caso já esteja cadastro acesso <a href="/accounts/activation-resend">Reenvie</a>""")
        # self.add_error('email', msg)
    def clean_email(self):
        # try:
        #     User.objects.get(email=email)
        # except User.DoesNotExist:
        #     return email
        # raise forms.ValidationError("A user with that username already exists123.")

        # usuario=User.objects.get(email__iexact=self.cleaned_data['email'])
        # if usuario.is_active==False:
        #     msg = format_html("""Caso já esteja cadastro acesso <a href="/accounts/activation-resend">Reenvie</a>""")
        #     self.add_error('email', msg)
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            usuario = User.objects.get(email__iexact=self.cleaned_data['email'])
            if usuario.is_active == False:
                msg = format_html(
                    """Caso já esteja cadastro acesso <a href="/accounts/activation-resend">Reenvie</a>""")
                raise forms.ValidationError(msg)
            else:
                raise forms.ValidationError(_("Este endereço de e-mail já está em uso. Forneça um endereço de e-mail diferente."))
        return self.cleaned_data['email']

    # def clean_email(self):
    #     """
    #     Validate that the supplied email address is unique for the
    #     site.
    #
    #     """
    #     if User.objects.filter(email__iexact=self.cleaned_data['email']):
    #         raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
    #     return self.cleaned_data['email']
class UserProfileForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #     # If you pass FormHelper constructor a form instance
    #     # It builds a default layout with all its fields
    #     self.helper = FormHelper(self)
    #     self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = UserProfile
        fields = ['nm_completo', 'nr_cpf_cgc', 'ds_codigo_conselho','foto_perfil', 'observacoes', 'tipo_usuario', 'nrTelCelular']
        # exclude = ['user']

