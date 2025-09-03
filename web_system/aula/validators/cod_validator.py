from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CodValidator:
    def __init__(self, cod='00000000'):
        self.code = cod

        def __call__(self):
            if valor == self.code:
                raise validationError(_('Valor Invalido').params('valor:', valor))


    def __eq__(self, other):
        return isinstance(other, CodValidator) and self.code == other.code