from django.shortcuts import HttpResponse
from django.views import View
from datetime import  datetime
from django.http import JsonResponse
from django.core.serializers import serialize

from relacionamentos.models import Reporter


class  Nome(View):
    @staticmethod
    def get(request, nome):
        dados = str(request.GET.get('type'))
        pessoas = Reporter.objects.find_by_nome(nome)

        if nome == '':
            return HttpResponse(status=400)

        if dados == 'json':
            pessoa = serialize('python', pessoas)
            return JsonResponse(list(pessoa),safe=False)

        elif dados == 'http':
            return HttpResponse(pessoas)

        else:
            return HttpResponse(status=400)






