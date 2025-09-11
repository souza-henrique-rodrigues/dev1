from .base_model import models, BaseModel
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date
from .reporter import Reporter
from .magazine import Magazine



class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    pub_date = models.DateField(null=True)
    reporter = models.ForeignKey(Reporter, on_delete = models.RESTRICT)
    magazines = models.ManyToManyField(Magazine,null=True ,blank=True)


def __str__(self):
    return f"{self.title} by {self.reporter.nome} : ({self.reporter.email}) "



def clean(self):

    today = date.today()

    try:
        if self.issue_date > today:
            raise ValidationError({'Data de cadastro invalida'}, code='error2')

    except ValueError:
        pass