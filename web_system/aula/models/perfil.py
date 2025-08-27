from .base_model import BaseModel
from django.db import  models


class Perfil(models.Model):
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    data_nascimento = models.DateField(help_text='Data de nascimento', verbose_name='Data de nascimento')
    bio = models.CharField(max_length=255)
    passaporte = models.CharField(max_length=10)

    # genero = tipo genero = enum model.textChoice 