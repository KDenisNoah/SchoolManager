from django.http import HttpResponse
from django.shortcuts import redirect, render
from teachers.models import Student, Teacher, Staff
from teachers.forms import StudentForm, TeacherForm, StaffForm

def students_page(request):
    if request.method == 'POST':
        #print(request.POST)
        if 'add_student' in request.POST:
            #print(request.POST)
            f = StudentForm(request.POST, request.FILES)
            #print(f)
            if f.is_valid():
                f.save()
        elif 'student' in request.POST:  # maybe redirect this to another view, maybe groups/selected group with a message with the added students
            for item in request.POST.getlist('student'):
                #print((item))  # add those pk to the (to be done) selected group
                s = Student.objects.get(id=item)
                # s.delete()
            f = StudentForm()
        else:
            f = StudentForm()
    else:
        f = StudentForm()

    students = Student.objects.all()
    return render(request, 'teachers/students.html', {'students': students, 'form': f})

def student_page(request,student_id=None):
    if not student_id:
       redirect(students_page)
    student = Student.objects.filter(pk=student_id)[0]
    return render(request, 'teachers/student.html', {'student': student})


def teachers_page(request):
    if request.method == 'POST':
        #print(request.POST)
        if 'add_teacher' in request.POST:
            #print(request.POST)
            f = TeacherForm(request.POST, request.FILES)
            #print(f)
            if f.is_valid():
                f.save()
        elif 'teacher' in request.POST:  # maybe redirect this to another view, maybe groups/selected group with a message with the added students
            for item in request.POST.getlist('teacher'):
                #print((item))  # add those pk to the (to be done) selected group
                s = Teacher.objects.get(id=item)
                # s.delete()
            f = TeacherForm()
        else:
            f = TeacherForm()
    else:
        f = TeacherForm()

    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers, 'form': f})


def staff_page(request):
    if request.method == 'POST':
        print(request.POST)
        if 'add_staff' in request.POST:
            #print(request.POST)
            f = StaffForm(request.POST, request.FILES)
            #print(f)
            if f.is_valid():
                f.save()
        elif 'staff' in request.POST:  # maybe redirect this to another view, maybe groups/selected group with a message with the added students
            for item in request.POST.getlist('staff'):
                #print((item))  # add those pk to the (to be done) selected group
                s = Staff.objects.get(id=item)
                # s.delete()
            f = StaffForm()
        else:
            f = StaffForm()
    else:
        f = StaffForm()

    staffs = Staff.objects.all()
    return render(request, 'teachers/staff.html', {'staffs': staffs, 'form': f})
