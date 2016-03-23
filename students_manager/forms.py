from django.forms import ModelForm, TextInput
from django import forms
from students_manager.models import Student, Group, Grouping


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name','last_name_1','last_name_2','picture','birthdate','educacode','uniquename','nationality','gender','email','picture']
        widgets = {
            'name': forms.TextInput,
            'last_name_1': TextInput,
            'last_name_2': TextInput,
            'uniquename': TextInput,
            'educacode': TextInput,
            'nationality': TextInput,
        }
        
        
class GroupForm(ModelForm):
   
   class Meta:
      model = Group
      fields = ['name','course']
      
      widgets = {
            'name': forms.TextInput,
            }
      
class GroupingForm(ModelForm):
   
   class Meta:
      model = Grouping
      fields = ['name','course']
      
      widgets = {
            'name': forms.TextInput,
            }      