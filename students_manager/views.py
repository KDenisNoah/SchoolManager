from django.http import HttpResponse
from django.shortcuts import redirect, render
from students_manager.models import Student, Group, Course, Grouping
from students_manager.forms import StudentForm, GroupForm, GroupingForm


def student_manager_page(request):
    return render(request, 'home.html')


def students_page(request):
    if request.method == 'POST':
        print(request.POST)
        if 'add_student' in request.POST:
            print(request.POST)
            f = StudentForm(request.POST, request.FILES)
            print(f)
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
       f = GroupForm(request.POST)
       if f.is_valid():
            f.save()
    else:
        f = GroupForm()
        

    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups, 'form': f})


def groupings_page(request):
    if request.method == 'POST':
       f = GroupingForm(request.POST)
       if f.is_valid():
            f.save()
    else:
        f = GroupingForm()
   
   
    groupings = Grouping.objects.all()
    d = {}
    for g in groupings:
       if not g.course in d.keys():
          d[g.course] = []
       d[g.course].append(g)
       print(d)
    return render(request, 'groupings.html', {'groupings': d, 'form': f})

def group_page(request,group_id=None):
    if not group_id:
       redirect(courses_page)
    group = Group.objects.filter(pk=group_id)[0]
    students = Student.objects.filter(group=group)
    return render(request, 'group.html', {'group': group, 'students': students})

def grouping_page(request,grouping_id=None):
    if not grouping_id:
       redirect(courses_page)
    grouping = Grouping.objects.filter(pk=grouping_id)[0] #if grouping_id does not exist raises an error because [0] of none (same in group)
    students = Student.objects.filter(groupings=grouping)
    return render(request, 'grouping.html', {'grouping': grouping, 'students': students})

def course_page(request,course_id=None):
    if not course_id:
       redirect(courses_page)
    course = Course.objects.filter(pk=course_id)[0]
    groups = Group.objects.filter(course=course_id)
    groupings = Grouping.objects.filter(course=course_id) #if grouping_id does not exist raises an error because [0] of none (same in group)
    students = Student.objects.filter(group=groups)
    return render(request, 'course.html', {'course': course, 'groups': groups,'groupings': groupings, 'students': students})
 
def courses_page(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['course_name'],year=request.POST['course_year'])
        return redirect(courses_page)

    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})