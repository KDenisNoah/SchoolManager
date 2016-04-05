from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.context_processors import csrf
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
    return render(request, 'timetable/timetable.html', {'timetable': timetable, 'form': f})

from django.views.decorators.csrf import csrf_exempt
from django import forms

@csrf_exempt
def timetable_ajax(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST' and request.is_ajax():
            data={'day': request.POST["day"],'hour': request.POST["hour"]}
            f = TimetableForm(initial=data)
            f.fields['day'] = forms.CharField(label="", widget=forms.HiddenInput())
            f.fields['hour'] = forms.CharField(label="", widget=forms.HiddenInput())
            if f.is_valid():
                print("valid")
                f.save()
    else:
        f = TimetableForm()
    c['form'] = f
    return render(request, 'timetable/ajax_form.html', c)
 

def grouping_page(request,grouping_id=None):
    if not grouping_id:
       redirect(timetable)
    timetable = Timetable.objects.filter(grouping=grouping_id)
    grouping = Grouping.objects.filter(id=grouping_id)[0]
    hours = ['1','2','3','FT','4','5','6','7']
    days = ['Mo','Tu','We','Th','Fr']   
    l=[]
    for h in hours:
      dl=[]
      for d in days:
        t=timetable.filter(hour=h,day=d)
        if len(t)==0:
          t=[]
          a={}
          a['hour']=h
          a['day']=d
          t.append(a)
        dl.append(t)
      l.append(dl)    
    return render(request, 'timetable/tgrouping.html', {'timetable': timetable,'hours':hours,'days':days, 'tt':l})
  
def teacher_timetable_page(request,teacher_id=None):
    if not teacher_id:
       redirect(timetable)
    timetable = Timetable.objects.filter(teacher=teacher_id)
    hours = ['1','2','3','FT','4','5','6','7']
    days = ['Mo','Tu','We','Th','Fr']
    #FIXME: Dirty hack to ensure that the timetable table is fully displayed. I create dummy day-hours combinations.
    l=[]
    for h in hours:
      dl=[]
      for d in days:
        t=timetable.filter(hour=h,day=d)
        if len(t)==0:
          t=[]
          a={}
          a['hour']=h
          a['day']=d
          t.append(a)
        dl.append(t)
      l.append(dl)
    return render(request, 'timetable/tgrouping.html', {'timetable': timetable,'hours':hours,'days':days,'tt':l})  