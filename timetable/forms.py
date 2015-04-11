from django.forms import ModelForm, TextInput
from django import forms
from timetable.models import Timetable


class TimetableForm(ModelForm):

    class Meta:
        model = Timetable
        fields = ['grouping','subject','hour','day']
        widgets = {
            'subject': forms.TextInput,
        }
        
        