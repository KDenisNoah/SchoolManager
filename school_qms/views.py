from django.http import HttpResponse
from django.shortcuts import redirect, render
from school_qms.models import *
from school_qms.forms import *


def qms_page(request):
    return render(request, 'qms_home.html')


def processes_page(request):
    if request.method == 'POST':
        Process.objects.create(name=request.POST['process_name'])
        return redirect(processes_page)

    processes = Process.objects.all()
    return render(request, 'processes.html', {'processes': processes})


def procedures_page(request, proc_id=None):
    if request.method == 'POST':
        f = ProcedureForm(request.POST)
        if f.is_valid():
            proc = f.save()
            return redirect('procedure', proc.pk)
    elif proc_id:
        procedure = Procedure.objects.get(pk=proc_id)
        f = ProcedureForm(instance=procedure)
    else:
        f = ProcedureForm()

    procedures = Procedure.objects.all()
    return render(request, 'procedures.html',
         {'procedures': procedures, 'form': f})


def documents_page(request, doc_id=None):
    if doc_id:
        print ((doc_id))
    if request.method == 'POST':
        f = DocumentForm(request.POST, request.FILES)
        if f.is_valid():
            doc = f.save()
            rev = Revision(document=doc, number=0, reason='initial creation')
            rev.save()
            return redirect('document', doc.pk)
    elif doc_id:
        document = Document.objects.get(pk=doc_id)
        f = DocumentForm(instance=document)
    else:
        f = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'documents.html',
         {'documents': documents, 'form': f})


def document_page(request, doc_id):
    doc = Document.objects.get(pk=doc_id)
    rev = Revision.objects.filter(document=doc.pk)
    return render(request, 'document.html', {'document': doc, 'revision': rev})


def procedure_page(request, proc_id):
    proc = Procedure.objects.get(pk=proc_id)
    docs = Document.objects.filter(procedure=proc)
    return render(request, 'procedure.html', {'procedure': proc,
         'documents': docs})


def add_agent(request):
    if request.method == 'POST':
        f = AgentForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = AgentForm()

    Agents = Agent.objects.all()
    return render(request, 'add_agent.html',
         {'Agents': Agents, 'form': f})


def add_recipient(request):
    if request.method == 'POST':
        f = RecipientForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = RecipientForm()

    Recipients = Recipient.objects.all()
    return render(request, 'add_recipient.html',
         {'Recipients': Recipients, 'form': f})


def add_revision(request, doc_id=None):
    if request.method == 'POST':
        f = RevisionForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        print((doc_id))
        if doc_id:
            rev = Revision.objects.filter(document=doc_id)
            n = max(r.number for r in rev) + 1
            data = {'document': doc_id, 'number': n}
            #maybe i should create another view,with the doc_id and number
            #locked, the way its done the could be changed
            f = RevisionForm(initial=data)
        else:
            f = RevisionForm()

    return render(request, 'add_revision.html', {'form': f})


def add_time(request):
    if request.method == 'POST':
        f = TimeForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = TimeForm()
        print((f))

    times = Times.objects.all()
    return render(request, 'add_times.html',
         {'Times': times, 'form': f})


def activity_page(request, proc_id=None):
    if request.method == 'POST':
        f = ActivityForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        if proc_id:
            initial = {'procedure': proc_id}
            f = ActivityForm(initial)
        else:
            f = ActivityForm()

    activities = Activity.objects.filter(procedure=proc_id)

    return render(request, 'activity.html', {
         'activities': activities, 'form': f})