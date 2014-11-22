from django.http import HttpResponse
from django.shortcuts import redirect, render
from school_qms.models import Process, Procedure, Document, Agent, Revision
from school_qms.forms import DocumentForm, AgentForm, RevisionForm


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


def documents_page(request):
    if request.method == 'POST':
        f = DocumentForm(request.POST, request.FILES)
        if f.is_valid():
            doc = f.save()
            rev = Revision(document=doc, number=0, reason='initial creation')
            rev.save()
    else:
        f = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'documents.html',
         {'documents': documents, 'form': f})


def document_page(request, doc_id):
    doc = Document.objects.get(pk=doc_id)
    rev = Revision.objects.filter(document=doc.pk)
    return render(request, 'document.html', {'document': doc, 'revision': rev})


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