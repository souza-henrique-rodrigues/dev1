from django.shortcuts import HttpResponse
from django.views import View
from datetime import  datetime

class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = 'boa noite'

        if 12 > agora.hour > 6:
            mensagem = 'Bom dia'

        elif 0 < agora.hour <= 6:
            mensagem = 'Boa madrugada'

        completo = f'<html> <h1> {mensagem.capitalize()} visitante </h1>  </html> '

        return HttpResponse(completo)