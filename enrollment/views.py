from django.http import HttpResponse
from django.shortcuts import redirect, render
from enrollment.models import Subject
from enrollment.forms import SubjectForm


def subjects_page(request,subject_id=None):
    if request.method == 'POST':
       #print(request.POST)
       f = SubjectForm(request.POST)
       if f.is_valid():
            f.save()
    elif subject_id:
        subjects = Subject.objects.get(pk=subject_id)
        f = SubjectForm(instance=group)
    else:
        f = SubjectForm()
        
    subjects = Subject.objects.all()
    return render(request, 'enrollment/subjects.html', {'subjects': subjects, 'form': f})

