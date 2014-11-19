from django.http import HttpResponse
from django.shortcuts import redirect, render
from school_qms.models import Process, Procedure


def qms_page(request):
    return render(request, 'qms_home.html')


def processes_page(request):
    if request.method == 'POST':
        Process.objects.create(name=request.POST['process_name'])
        return redirect(processes_page)

    processes = Process.objects.all()
    return render(request, 'processes.html', {'processes': processes})


def procedures_page(request):
    if request.method == 'POST':
        Procedure.objects.create(name=request.POST['procedure_name'])
        return redirect(procedures_page)

    procedures = Procedure.objects.all()
    return render(request, 'procedures.html', {'procedures': procedures})
