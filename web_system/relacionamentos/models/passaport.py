from .base_model import models, BaseModel
from relacionamentos.validators.funcoes import validate_cpf
from django.core.exceptions import ValidationError
from datetime import date
from .person import Person



class Passaport(BaseModel):
    number = models.IntegerField(max_length=10, null=True)
    issue_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    owner = models.OneToOneField(Person, on_delete=models.CASCADE)


def __str__(self):
    return self.number


def clean(self):

    today = date.today()

    try:
        if self.issue_date > today:
            raise ValidationError({'Data de cadastro invalida'}, code='error2')

    except ValidationError:
        pass