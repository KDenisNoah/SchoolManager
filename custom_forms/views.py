from django.http import HttpResponse
from django.shortcuts import redirect, render
from custom_forms.models import CForm,Question,FormResponses
from custom_forms.forms import CFormForm, QuestionForm, ResponsesForm


def forms_page(request):
    if request.method == 'POST':
            f = CFormForm(request.POST)
            print(f)
            if f.is_valid():
                f.save()
    else:
        f = CFormForm()

    forms = CForm.objects.all()
    return render(request, 'forms.html', {'forms': forms, 'form': f})


def form_page(request,form_id=None):
    if not form_id:
       redirect(forms_page)
    form = CForm.objects.filter(pk=form_id)[0]
    questions = Question.objects.filter(form=form)
    return render(request, 'form.html', {'form': form, 'questions': questions})