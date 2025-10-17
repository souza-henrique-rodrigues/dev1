from relacionamentos.models import Reporter
from django.shortcuts import render, get_object_or_404, redirect


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
            reporter_id = request.POST.get('reporter_id',None)
            if int(reporter_id) == id:
                reporter.delete()
                return redirect('relacionamentos:reporter_function_list')
        else:
            context = {
                'reporter': reporter,
            }
            return render(request, 'reporter/delete.html',context)
    except:
        context = {}
        return render(request, 'reporter/list.html', context)



