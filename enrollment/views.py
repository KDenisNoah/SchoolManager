from django.http import HttpResponse
from django.shortcuts import redirect, render
from enrollment.models import Subject, Enrollment
from enrollment.forms import SubjectForm, EnrollmentForm


def subjects_page(request,subject_id=None):
    if request.method == 'POST':
       #print(request.POST)
       f = SubjectForm(request.POST)
       if f.is_valid():
            f.save()
       f = SubjectForm()
    elif subject_id:
        subject = Subject.objects.get(pk=subject_id)
        f = SubjectForm(instance=subject)
    else:
        f = SubjectForm()
        
    subjects = Subject.objects.all()
    return render(request, 'enrollment/subjects.html', {'subjects': subjects, 'form': f})

def enrollments_page(request,enrollment_id=None):
    if request.method == 'POST':
       #print(request.POST)
       f = EnrollmentForm(request.POST)
       if f.is_valid():
            f.save()
       f = EnrollmentForm()
    elif enrollment_id:
        enrollment = Enrollment.objects.get(pk=enrollment_id)
        f = EnrollmentForm(instance=enrollment)
    else:
        f = EnrollmentForm()
        
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment/enrollments.html', {'enrollments': enrollments, 'form': f})

