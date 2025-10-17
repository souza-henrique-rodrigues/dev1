from django.db.models import QuerySet
from .base_manager import BaseManager
from datetime import  date



class ReporterManager(BaseManager):

    def find_by_nome(self, nome: str) -> list['Reporter']:
        if isinstance(nome, str) and len(nome) > 0:
            consulta = self.filter(nome__icontains=nome).order_by('nome')[:2]
            return list(consulta)
        else:
            raise TypeError('O nome deve ser uma String maior que 0')


    def find_by_publication_date(self, publication_date: date) -> QuerySet['Reporter']:
        if isinstance(publication_date, date):
            today = date.today()
            consulta = self.filter(article__pub_date__range=(publication_date, today))
            return consulta

        else:
            raise ValueError('Data errada')


