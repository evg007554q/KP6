from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    """ Пользователи """
    username = None

    email = models.EmailField(unique=True, verbose_name='e-mail ')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', null=True, blank=True)
    country = models.CharField(max_length=10, verbose_name='Страна', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', null=True, blank=True)
    key_user = models.CharField(max_length=12, verbose_name='Ключ', null=True, blank=True)

    active_user = models.BooleanField(default=False, verbose_name='признак активного пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []