"""controle_hc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    path('', views.home, name='home'),
    path('api/', include('blog.urls')),
    
    

  


    re_path(r'^prestador/', include(('usuarios.urls', 'usuarios'),namespace='usuarios')),
    re_path(r'^prestador/', include(('prestadores.urls','prestadores'),namespace='prestadores')),
    re_path(r'^select2/', include('django_select2.urls')),
    
  
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
