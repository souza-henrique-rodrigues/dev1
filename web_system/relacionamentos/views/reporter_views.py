from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.http import require_http_methods
from relacionamentos.models import Reporter
from relacionamentos.forms import ReporterForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


class ReporterListView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamentos.view_reporter'

    @staticmethod
    def get(request):
        reporters = Reporter.objects.all()
        context = {
            'reporters': reporters
        }
        return render(request, 'reporter/list.html', context)



class ReporterDetailView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamentos.view_reporter_views'


    @staticmethod
    def get(request, id):
        reporter = Reporter.objects.get(pk=id)

        context = {
            'reporter': reporter
        }

        return render(request, 'reporter/read.html', context)



class ReporterUpdateView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = reverse_lazy('accounts:login')
    permission_required = 'relacionamentos.view_reporter'

    @staticmethod
    def get(request,id):
        reporter = get_object_or_404(Reporter, pk=id)
        form = ReporterForm(instance=reporter)
        context = {
            'form':form,
            'reporter':reporter
        }
        return render(request,'reporter/update.html',context)

    @staticmethod
    def post(request,id):
        reporter = get_object_or_404(Reporter, pk=id)
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_class_list')
        context = {
            'form':form,
            'reporter':reporter
        }
        return render(request,'reporter/update.html',context)



































