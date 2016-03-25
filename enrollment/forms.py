from django.forms import ModelForm, TextInput
from django import forms
from groups.models import Course
from enrollment.models import Subject,Enrollment


class SubjectForm(ModelForm):
   error_css_class = 'bg-danger'
   required_css_class = 'text-warning'

   class Meta:
      model = Subject
      fields = ['name','shortname', 'abv','course','stype']
      
      widgets = {
            'name': forms.TextInput,
            'shortname': forms.TextInput,
            'abv': forms.TextInput,
            }
      
class EnrollmentForm(ModelForm):
   error_css_class = 'bg-danger'
   required_css_class = 'text-warning'

   class Meta:
      model = Enrollment
      fields = ['student','course', 'year','subjects']
