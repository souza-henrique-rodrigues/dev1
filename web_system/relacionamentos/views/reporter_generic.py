from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from relacionamentos.models import Reporter
from relacionamentos.forms import ReporterForm



class ReporterGenericList(ListView):
    model = Reporter
    template_name = 'reporter/list.html'
    context_object_name = 'reporters'
    queryset = Reporter.objects.find_by_nome('Henrique')


class ReporterGenericRead(DetailView):
    model = Reporter
    fields = '__all__'
    template_name = 'reporter/read.html'
    success_url = reverse_lazy('relacionamentos:reporter_generic_list')


class ReporterGenericDelete(DeleteView):
    model = Reporter
    fields = '__all__'
    template_name = 'reporter/delete.html'
    success_url = reverse_lazy('relacionamentos:reporter_generic_list')


class ReporterGenericCreate(CreateView):
    model = Reporter
    form_class = ReporterForm
    template_name = 'reporter/create.html'
    success_url = reverse_lazy('relacionamentos:reporter_generic_list')

class ReporterGenericUpdate(UpdateView):
    model = Reporter
    fields = '__all__'
    form_class = ReporterForm
    template_name = 'reporter/update.html'
    success_url = reverse_lazy('relacionamentos:reporter_class_update')




























