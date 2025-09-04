from .base_model import BaseModel
from django.db import  models
from dajngo.core.validators import MaxValueValidator, MinValueValidator

#adicionar help_text e verbose

class Avaliacao(BaseModel):
    titulo = models.CharField(max_length=100)
    data_avaliacao = models.DateField()
    data_vista = models.DateField()
    comentario = models.TextField()
    nota = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    acompanhates = models.CharField()
    likes = models.IntegerField()




