from .base_model import models, BaseModel
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date


class Magazine(models.Model):
    nome = models.CharField(max_length=100)
    edicao = models.IntegerField()
