from .base_model import models, BaseModel
from django.core.validators import MinLengthValidator
from relacionamentos.validators import validate_cpf
from django.core.exceptions import ValidationError
from datetime import date



class Person(BaseModel):
    nome = models.Charfield(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.Charfield(max_length=100, validators=[MinLengthValidator(11), validate_cpf])




    def clean(self):
        today = date.today()

        try :
            if self.data_nascimento > today.replace(year=today.year - 18):
                raise ValidationError({'data_nascimento': _('Você deve ser maior de 18 anos')}, code='error1')

        except ValueError:
            pass