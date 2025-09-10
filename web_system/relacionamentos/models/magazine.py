from .base_model import models, BaseModel
from django.core.validators import MinLengthValidator
from relacionamentos.validators import validate_cpf
from django.core.exceptions import ValidationError
from datetime import date


class Magazine(models.Model):
    nome = models.charField()
    edicao = models.DateField()
