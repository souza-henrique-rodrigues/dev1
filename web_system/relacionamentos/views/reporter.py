from relacionamentos.models import Reporter
from django.shortcuts import render, get_object_or_404, redirect
from relacionamentos.forms import ReporterForm


def reporter_list(request):
    reporters = Reporter.objects.all()

    context = {
        'reporters': reporters,
    }

    return render(request,'reporter/list.html', context)



def reporter_detail(request,pk):
    reporter = Reporter.objects.get(id=pk)
    context = {
        'reporter': reporter,
    }
    return render(request, 'reporter/read.html',context)



def reporter_delete(request,id):
    reporter = get_object_or_404(Reporter, pk=id)

    try:
        if request.method == 'POST':
            reporter_id = request.POST.get('id',None)
            if int(reporter_id) == id:
                reporter.delete()
                return redirect('relacionamentos:reporter_function_list')
        else:
            context = {
                'reporter': reporter,
            }
            return render(request, 'reporter/delete.html',context)
    except Exception as e:
        print(e)
        context = {}
        return render(request, 'reporter/list.html', context)


def reporter_change_name(request,id):
    reporter = get_object_or_404(Reporter, pk=id)
    try:
        new_name = str(reporter.nome) + 'john doe'
        reporter.nome = new_name
        reporter.save()

        return redirect('relacionamentos:reporter_function_list')

    except Exception as e :
        print(e)
        print('Erro ao trocar nome do reporter')
        return redirect('relacionamentos:reporter_function_list')





def reporter_create(request):
    if request.method == 'POST':
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_function_list')
    else:
        form = ReporterForm()
    context = {
        'form':form
    }
    return render(request, 'reporter/create.html',context)



def reporter_update(request, id):
    reporter = get_object_or_404(Reporter, pk=id)

    if request.method == 'POST':
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_function_list')
    else:
        form = ReporterForm(instance=reporter)
    context = {
        'form': form,
        'reporter': reporter
    }
    return render(request, 'reporter/update.html', context)




































