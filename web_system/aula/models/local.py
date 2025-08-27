from .base_model import BaseModel
from django.db import  models

#adicionar help_text e verbose

class Local(BaseModel):
    nome = models.CharField(max_length=100)
    informacoes = models.TextField()
    endereco = models.CharField(max_length=200)
    nota = models.FloatField()
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
    ingresso = models.BooleanField()
    valor = models.DecimalField(max_length=10, decimal_places=2, null=True, blank=True)
    acessibilidade = models.BooleanField()
    classificacao = models.IntegerField()
    contato = models.EmailField()


    def __str__(self):
        return f"{self.nome}"

