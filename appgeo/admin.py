from django.contrib import admin
from . import models 


# Register your models here.

class GeoAdmin(admin.ModelAdmin):
    list_display = ('name','position')

admin.site.register(models.localizacao, GeoAdmin)