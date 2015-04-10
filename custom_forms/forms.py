from django.forms import ModelForm, TextInput
from django import forms
from custom_forms.models import CForm,Question,FormResponses


class CFormForm(ModelForm):

    class Meta:
        model = CForm
        fields = ['name']
        
        widgets = {
            'name': forms.TextInput,
        }
        
class QuestionForm(ModelForm):
   
   class Meta:
      model = Question
      fields = ['form','question','qtype','options','enabled','order_in_form']
      
      
class ResponsesForm(ModelForm):
   
   class Meta:
      model = FormResponses
      fields = ['question','value','form_instance']
      