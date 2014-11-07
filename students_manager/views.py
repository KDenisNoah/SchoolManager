from django.http import HttpResponse
from django.shortcuts import redirect, render
from students_manager.models import Student


def home_page(request):
    if request.method == 'POST':
        Student.objects.create(text=request.POST['student_text'])
        return redirect('/')

    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})
