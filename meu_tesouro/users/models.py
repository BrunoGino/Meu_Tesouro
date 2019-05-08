# Django imports
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


# Core imports
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Método privado, cria um usuário e salva no banco com os parâmetros indicados

        :param email:
        :param password:
        :param is_staff:
        :param is_superuser:
        :param extra_fields:
        :return:
        """
        now = timezone.now()

        if not email:
            raise ValueError('O e-mail deve ser informado!')

        email = self.normalize_email(email)
        user = self.model(
            email=email, is_staff=is_staff,
            is_active=True, is_superuser=is_superuser,
            last_login=now, date_joined=now, **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Cria um usuário comum
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Cria um usuário com permissões de administrador
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Definição de classe base de usuário, substituindo a default dada pelo django
    """
    email = models.EmailField(max_length=90, unique=True, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    cpf = models.CharField(max_length=14, blank=False)
    birthday = models.DateField(blank=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf', 'birthday']

    object = UserManager()

    def __str__(self):
        return self.first_name

    class Meta:
        """
        Traduz a palavra usuário e usuários
        """
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/user/%s/" % self.email

    def get_full_name_(self):
        """
        Retorna o nome completo do usuário
        :return:
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        """
        Retorna o primeiro nome do usuário
        :return:
        """
        return self.first_name


