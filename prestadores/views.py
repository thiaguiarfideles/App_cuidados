from django.shortcuts import render
from django.shortcuts import redirect
from usuarios.models import User
# Create your views here.
from .models import PrestadorPessoaFisica

from .forms import PrestadorPessoaFisicaForm, DadosPessoaisForm
from django.shortcuts import get_object_or_404
from django.core import serializers


def sucesso2(request):
    return render(request, 'sucesso.html')

def cadastro_prestador_pf(request):
    if request.method == "POST":
        form = PrestadorPessoaFisicaForm(request.POST, request.FILES,request.user)
        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.user = request.user
            prestador.save()
            return redirect('cadastro/sucesso')
    else:
        form = PrestadorPessoaFisicaForm()
    return render(request, 'cadastro_pessoa_fisica.html', {
        'form': form
    })
def dados_pessoais(request):
    if request.method == "POST":
        form = DadosPessoaisForm(request.POST, request.FILES)
        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.usuario = request.user
            prestador.save()
            # prestador.save()
            return redirect('sucesso')
    else:
        form = DadosPessoaisForm()
    return render(request, 'dados_pessoais.html', {
        'form': form
    })



def cadastros_list(request):
    usuario = request.user
    cadastros = PrestadorPessoaFisica.objects.filter(user=usuario.id).order_by('-created_at')
    return render(request,'cadastros_list.html',{
        'cadastros':cadastros
    })

def cadastro_enviado(request,pk):
    cadastro=get_object_or_404(PrestadorPessoaFisica,pk=pk)
    data = serializers.serialize("python", PrestadorPessoaFisica.objects.filter(pk=pk))
    return render(request,'cadastro_detail.html',{'cadastro':cadastro,'data':data})


