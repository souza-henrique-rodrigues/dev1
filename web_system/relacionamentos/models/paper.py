from .base_model import models, BaseModel
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date
from .reporter import Reporter
from .magazine import Magazine



class Paper(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete = models.RESTRICT)
    magazines = models.ManyToManyField(Magazine,null=True ,blank=True, through='Publication', through_fields=('paper', 'magazine'))

