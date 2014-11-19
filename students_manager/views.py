from django.http import HttpResponse
from django.shortcuts import redirect, render
from students_manager.models import Student, Group
from students_manager.forms import StudentForm


def student_manager_page(request):
    return render(request, 'home.html')


def students_page(request):
    if request.method == 'POST':
        if 'add_student' in request.POST:
            f = StudentForm(request.POST, request.FILES)
            if f.is_valid():
                f.save()
        elif 'student' in request.POST:  # maybe redirect this to another view, maybe groups/selected group with a message with the added students
            for item in request.POST.getlist('student'):
                print((item))  # add those pk to the (to be done) selected group
                s = Student.objects.get(id=item)
                # s.delete()
            f = StudentForm()
        else:
            f = StudentForm()
    else:
        f = StudentForm()

    students = Student.objects.all()
    return render(request, 'students.html', {'students': students, 'form': f})


def groups_page(request):
    if request.method == 'POST':
        Group.objects.create(name=request.POST['group_name'])
        return redirect(groups_page)

    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})