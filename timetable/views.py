from django.http import HttpResponse
from django.shortcuts import redirect, render
from students_manager.models import Student, Group, Course, Grouping
from timetable.models import Timetable
from timetable.forms import TimetableForm

def timetable_page(request):
    if request.method == 'POST':
            f = TimetableForm(request.POST)
            if f.is_valid():
                f.save()
    else:
        f = TimetableForm()

    timetable = Timetable.objects.all()
    return render(request, 'timetable.html', {'timetable': timetable, 'form': f})
 

def grouping_page(request,grouping_id=None):
    if not grouping_id:
       redirect(timetable)
    timetable = Timetable.objects.filter(grouping=grouping_id)
    grouping = Grouping.objects.filter(id=grouping_id)[0]
    matrix = {}
    for t in timetable:
       if not t.hour-1 in matrix.keys():
          matrix[t.hour-1]={}
       matrix[t.hour-1][t.day-1] = t.subject
    a = []
    for k in matrix.keys():
      b = []
      for i in range(len(matrix[k])):
         if i in matrix[k].keys():
            b.append(matrix[k][i])
         else:
            b.append("")
      a.append(b)

      
    #print(timetable)
    return render(request, 'tgrouping.html', {'timetable': timetable, 'matrix':a, 'days':range(len(a)), 'hours':range(len(a[0])), 'grouping': grouping})
 
