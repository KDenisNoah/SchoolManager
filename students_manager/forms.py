from django.forms import ModelForm, TextInput
from django import forms
from students_manager.models import Student, Group


class StudentForm(ModelForm):

    class Meta:
        model = Student
        widgets = {
            'name': forms.TextInput,
            'last_name_1': TextInput,
            'last_name_2': TextInput,
        }