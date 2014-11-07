from django.http import HttpResponse
from django.shortcuts import render
from students_manager.models import Student


def home_page(request):
    if request.method == 'POST':
        new_student_text = request.POST.get('student_text', '')
        Student.objects.create(text=new_student_text)
    else:
        new_student_text = ''

    return render(request, 'home.html', {
        'new_student_text': new_student_text,
    })
