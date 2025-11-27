from ..forms.contact_form import ContactForm
from django.shortcuts import render



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender')
            cc_myself = form.cleaned_data.get('cc_myself')

            recipients = ['@restinga.ifrs.edu.br']
            if cc_myself:
                recipients.append(sender)
            #implementar envio de e-mail

            context = {
                'recipients': recipients,
                'form': form,
                }
            return render(request,'contact/thanks.html', context)

        context = {'form':form, 'url_form': 'contact_function',}

        return render(request, 'contact/contact.html', context)

    elif request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form,
            'url_form': 'contact_function',
        }
        return render(request, 'contact/contact.html', context)

'''
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['ricardo.santos@restinga.ifrs.edu.br']
        
        if cc_myself:
            recipients = recipients.append(sender)

        contexto = {
        'form': form,
        'recipients': recipients,
        }
        return render(request, 'contact/thanks.html', contexto)
        
        contexto = {
        'form': form,
        'url_form': 'funcao_contato'
        }
        return render(request, 'contact/page_contact.html', contexto)

        elif request.method == 'GET':
            form = ContactForm()
            contexto = {
            'form': form,
            'url_form': 'funcao_contato'
            }
            return render(request, 'contact/page_contact.html', contexto)
'''