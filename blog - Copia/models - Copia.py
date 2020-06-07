from django.db import models
from django.utils import timezone
from usuarios.models import User
from django.urls import reverse
from django.conf import settings


# Create your models here.

class Post (models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250, verbose_name="Titulo")
    excerpt = models.TextField(null=True, verbose_name="Adicionar Texto")
    slug = models.SlugField(max_length=250,verbose_name="Apelido" ,unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now, verbose_name="Data da Publicação")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager


    def get_absolute_url(self):
        return reverse('blog:post_single',args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


 