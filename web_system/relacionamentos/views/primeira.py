from django.shortcuts import HttpResponse
from django.views import View



class Primeira(View):
    @staticmethod
    def get(request):
        mensagem = 'Ola sem bem vindo DEV'
        return HttpResponse(mensagem)
