from django.http import HttpResponse
from django.shortcuts import redirect, render
from students_manager.models import Student, Group


def home_page(request):
    return render(request, 'home.html')


def students_page(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['student_name'])
        return redirect('/students')

    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def groups_page(request):
    if request.method == 'POST':
        Group.objects.create(name=request.POST['group_name'])
        return redirect('/groups')

    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})