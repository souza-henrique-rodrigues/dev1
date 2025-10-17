from datetime import datetime
from django.shortcuts import HttpResponse

def saudacao(request):
    agora = datetime.now()
    mensagem = 'Boa noite'

    if 12 > agora.hour >6:
        mensagem = 'Bom dia'

    elif 0 < agora.hour <=6:
        mensagem = 'Boa madrugada'

    completo = f'<html> <h1> {mensagem.capitalize()} visitante </h1>  </html> '

    return HttpResponse(completo)