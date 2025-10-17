from .base_model import models, BaseModel
from django.core.validators import MinLengthValidator
from relacionamentos.validators.funcoes import validate_cpf
from django.core.exceptions import ValidationError
from datetime import date
from relacionamentos.managers import ReporterManager


class Reporter(BaseModel):
    #adicionar o cpf validator no campo cpf
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=120)
    email = models.EmailField()


    objects = ReporterManager()


    def __str__(self):
        return f'{self.nome} - {self.cpf} - {self.email}'


    def clean(self):
        forbiden_names = ['teste', 'Teste']

        try:
            if self.nome in forbiden_names:
                raise ValidationError({'nome': _('Nome não pode ser teste')}, code='error1')
        except :
            pass






