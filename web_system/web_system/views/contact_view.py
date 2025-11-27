from django.shortcuts import render
from django.views import View
from ..forms.contact_form import ContactForm


class ContactView(View):
    @staticmethod
    def get(request):
        form = ContactForm
        context = {
            'form':form,
            'url_form': 'class_contact'
        }
        return render(request,'contact/contact.html',context)

    @staticmethod
    def post(request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender')
            cc_myself = form.cleaned_data.get('cc_myself')

            recipients = ['@restinga.ifrs.edu.br']
            if cc_myself:
                recipients.append(sender)
            # implementar envio de e-mail

            context = {
                'recipients': recipients,
                'form': form,
            }
            return render(request, 'contact/thanks.html', context)

        context = {'form': form, 'url_form': 'contact_function', }

        return render(request, 'contact/contact.html', context)