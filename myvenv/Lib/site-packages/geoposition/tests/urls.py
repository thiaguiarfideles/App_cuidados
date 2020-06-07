from django.conf.urls import include, url
from django.contrib import admin
from example.views import poi_list

from example import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', poi_list),
    url(r'^admin/', admin.site.urls),
]
