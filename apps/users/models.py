from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField('teléfono', max_length=20, blank=True)
    avatar = models.ImageField('avatar', upload_to='avatars/', blank=True, null=True)
    balance = models.DecimalField('saldo', max_digits=10, decimal_places=2, default=0.00)
    country = models.CharField('país', max_length=100, blank=True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.username
