from django.forms import ModelForm, TextInput
from django import forms
from groups.models import Course, Group, Grouping, Group_Membership, Grouping_Membership
from orgperson.models import Student


class GroupForm(ModelForm):
   error_css_class = 'bg-danger'
   required_css_class = 'text-warning'

   class Meta:
      model = Group
      fields = ['name','course', 'year']
      
      widgets = {
            'name': forms.TextInput,
            }
      
class GroupMembershipForm(ModelForm):
   
   class Meta:
      model = Group_Membership
      fields = ['group','student']
      
class GroupingForm(ModelForm):
   
   class Meta:
      model = Grouping
      fields = ['name','course','year']
      
      widgets = {
            'name': forms.TextInput,
            }      

class GroupingMembershipForm(ModelForm):
   
   class Meta:
      model = Grouping_Membership
      fields = ['group','student']
            