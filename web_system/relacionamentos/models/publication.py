from django.db import models
from .base_model import BaseModel
from .magazine import Magazine
from .paper import Paper
from .person import Person




class Publication(BaseModel):
    magazine = models.ForeignKey(Magazine, on_delete=models.RESTRICT)
    paper = models.ForeignKey(Paper, on_delete=models.RESTRICT)
    editor = models.ForeignKey(Person, on_delete=models.RESTRICT)
    date = models.DateField()
    obs = models.TextField()


def __str__(self):
    return f'{self.magazine} - {self.paper} - {self.editor}'





