from .base_model import BaseModel
from django.db import  models
from aula.validators import validate_par
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

#adicionar help_text e verbose


class Atividade(BaseModel):
    nome = models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    turno = models.CharField(max_length=8,null=True,blank = True)
    nota = models.FloatField(default=0.0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    duracao = models.TimeField(verbose_name='Duração')
    ingresso = models.BooleanField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, null= True, blank=True)
    informacoes = models.TextField()
    guia = models.BooleanField()
    endereco = models.CharField(max_length=100,null=True,blank=True)
    participantes = models.IntegerField()


    def __str__(self):
        return  f"{self.id} - {self.nome}"

