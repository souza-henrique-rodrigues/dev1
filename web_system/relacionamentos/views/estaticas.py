from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from datetime import datetime
from django.http import JsonResponse

def saudacao(request):
    agora = datetime.now()
    mensagem = 'Boa noite'

    if 12 > agora.hour > 6:
        mensagem = 'Bom dia'

    elif 0 < agora.hour <= 6:
        mensagem = 'Boa madrugada'

    completo = f'<html> <h1> {mensagem.capitalize()} visitante </h1>  </html> '

    return HttpResponse(completo)


def primeira_view(request):
    contexto = {
        'mensagem': 'Ola dev'
    }
    return render(request, 'primeira.html', contexto)

'''
def nome(request, name):
    exemplo = Exemplo.objects.find_by_nome(name)
    objeto = serializers.serialize('python', exemplo)
    return JsonResponse(objeto, safe=False)
'''

def home(request):
    contexto = {
        'mensagem':'Ola seja bem vindo a home'
    }

    return render(request, 'home.html', contexto)


def senha(request,senha):

    mensagem = 'ola'
    return HttpResponse(mensagem)


