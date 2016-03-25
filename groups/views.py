from django.http import HttpResponse
from django.shortcuts import redirect, render
from groups.models import Student, Group, Course, Grouping
from groups.forms import GroupForm, GroupingForm,GroupingMembershipForm, GroupMembershipForm

def main_page(request):
    return render(request, 'groups/main_index.html')


def groups_page(request,group_id=None):
    if request.method == 'POST':
       #print(request.POST)
       f = GroupForm(request.POST)
       if f.is_valid():
            f.save()
    elif group_id:
        group = Group.objects.get(pk=group_id)
        f = GroupForm(instance=group)
    else:
        f = GroupForm()
        
    groups = Group.objects.all()
    return render(request, 'groups/groups.html', {'groups': groups, 'form': f})



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
    if request.method == 'POST':
       #print(request.POST)
       f = GroupMembershipForm(request.POST)
       if f.is_valid():
            f.save()
    elif group_id:
        group = Group.objects.get(pk=group_id)
        f = GroupMembershipForm(instance=group)
    else:
        f = GroupMembershipForm()
    group = Group.objects.filter(pk=group_id)[0] #if grouping_id does not exist raises an error because [0] of none (same in group)
    students = Student.objects.filter(group=group)
    return render(request, 'group.html', {'group': group,'form':f, 'students': students})#FIXME when a student is added in a grouping redirect to that group?

def grouping_page(request,grouping_id=None):
    if request.method == 'POST':
       #print(request.POST)
       f = GroupingMembershipForm(request.POST)
       if f.is_valid():
            f.save()
    elif grouping_id:
        grouping = Grouping.objects.get(pk=grouping_id)
        f = GroupingMembershipForm(instance=grouping)
    else:
        f = GroupingMembershipForm()
    grouping = Grouping.objects.filter(pk=grouping_id)[0] #if grouping_id does not exist raises an error because [0] of none (same in group)
    students = Student.objects.filter(grouping=grouping)
    return render(request, 'grouping.html', {'grouping': grouping,'form':f, 'students': students})#FIXME when a student is added in a grouping redirect to that grouping?

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