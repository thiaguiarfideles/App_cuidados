from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from core.helpers import validate_CPF

def foto_perfil_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.user.email, "perfil_"+filename)

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('endereço de email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nm_completo = models.CharField(verbose_name="Nome Completo", max_length=100,null=True, blank=True)
    nr_cpf_cgc = models.CharField(verbose_name="CPF",max_length=11,null=True, blank=True,validators=[validate_CPF])
    ds_codigo_conselho = models.CharField(verbose_name="Código do Conselho", max_length=10,blank=True, null=True)
    foto_perfil = models.ImageField(upload_to=foto_perfil_directory_path, null=True, blank=True)
    telefone = models.IntegerField(default=0)
    cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True,verbose_name="Observações")

    def __str__(self):
       return str(self.nm_completo)


    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfis"


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

  