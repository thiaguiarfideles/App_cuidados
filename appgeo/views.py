
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from appgeo.models import localizacao
from appgeo.forms import localizacaoForm

User = settings.AUTH_USER_MODEL

@login_required
def index(request):
    return render(request,'appgeo/index.html')
@login_required
def localizacao_view(request):
    form = localizacaoForm()

    if request.method == 'POST':
        form = localizacaoForm(request.POST, request.FILES, request.user)

        if form.is_valid():
            prestador = form.save(commit=False)
            prestador.user = request.user
            prestador.save()
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'appgeo/geolocalizador.html',{'form': form})    