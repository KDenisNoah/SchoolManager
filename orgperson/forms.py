from django.forms import ModelForm, TextInput
from django import forms
from orgperson.models import Teacher, Staff, Student


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = ['name','last_name_1','last_name_2','educacode','uniquename','gender','email','picture']
        widgets = {
            'name': forms.TextInput,
            'last_name_1': TextInput,
            'last_name_2': TextInput,
            'uniquename': TextInput,
            'educacode': TextInput,
        }
        
        
class StaffForm(ModelForm):

    class Meta:
        model = Staff
        fields = ['name','last_name_1','last_name_2','educacode','uniquename','gender','email','picture','stype']
        widgets = {
            'name': forms.TextInput,
            'last_name_1': TextInput,
            'last_name_2': TextInput,
            'uniquename': TextInput,
            'educacode': TextInput,
        }
        
        
class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name','last_name_1','last_name_2','picture','birthdate','educacode','uniquename','gender','email','nationality']
        widgets = {
            'name': forms.TextInput,
            'last_name_1': TextInput,
            'last_name_2': TextInput,
            'uniquename': TextInput,
            'educacode': TextInput,
        }
        
        