from relacionamentos.forms import BaseForm
from relacionamentos.models import Reporter



class ReporterForm(BaseForm):
    '''
    fields especifica quais campos do model vão ir para o form final
    se necessários menos campos usar uma lista e informas campos = [nome, cpf, idade ]....
    '''
    class Meta:
        model = Reporter
        fields = '__all__'

