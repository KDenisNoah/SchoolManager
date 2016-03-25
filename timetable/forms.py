from django.forms import ModelForm, TextInput
from django import forms
from timetable.models import Timetable


class TimetableForm(ModelForm):
    error_css_class = 'bg-danger'
    
    class Meta:
        model = Timetable
        fields = ['grouping','subject','teacher','hour','day']
        
        