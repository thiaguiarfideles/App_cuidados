python manage.py shell
from django.contrib.sites.models import Site
print(Site.objects.get(name='example.com').id)