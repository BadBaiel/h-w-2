from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ADMIN = 1
VIPClient = 2
Client = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (Client, "Client")
)

MALE = 1
FEMALE = 2
OTHER = 3

USER_GENDER = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER")
)
class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователи',
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя'),
    phone_number = models.CharField('номер телефона', max_length=20),
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=USER_GENDER, verbose_name='Пол')
