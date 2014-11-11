from django.http import HttpResponse
from django.shortcuts import redirect, render
from students_manager.models import Student


def home_page(request):
    return render(request, 'home.html')

def students_page(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['student_name'])
        return redirect('/students')

    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})