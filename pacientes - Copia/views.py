
from django.shortcuts import render
from pacientes.models import DadosPaciente
from pacientes.forms import DadosPacienteForm



def index(request):
    return render(request,'pacientes/index.html')

def cadastrar_paciente_view(request):
    form = DadosPacienteForm()

    if request.method == 'POST':
        form = DadosPacienteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'pacientes/pacientes.html',{'form': form})    