from django.forms import *  # ModelForm, TextInput, CheckboxSelectMultiple
from django import forms
from school_qms.models import *

class processForm(ModelForm):
    
    class Meta:
        model = Process
        fields = ['name','code','rev','owner','description','scope','start_activity','providers','end_activity','customers','subprocess','instructions','legislation','date']
        
        
class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ['procedure', 'code', 'name', 'description', 'record',
            'enabled', 'disabled_date', 'creation_date', 'aprobation_date',
            'document_file', 'document_url', 'owner', 'recipients',
             'when_distribute']
        widgets = {
            'procedure': Select(attrs={'class': 'form-control'}),
            'code': TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'enabled': CheckboxInput(attrs={'class': 'form-control'}),
            'disabled_date': DateInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control',
                 'rows': '4'}),
            'creation_date': DateInput(attrs={'class': 'form-control'}),
            'aprobation_date': DateInput(attrs={'class': 'form-control'}),
            'document_url': URLInput(attrs={'class': 'form-control'}),
            'document_file': FileInput(attrs={'class': 'form-control'}),
            'owner': Select(attrs={'class': 'form-control'}),
            'recipients': SelectMultiple(attrs={'class': 'form-control'}),
            'when_distribute': SelectMultiple(attrs={'class': 'form-control'}),
        }


class AgentForm(ModelForm):

    class Meta:
        model = Agent
        fields = ['name']
        widgets = {
            'name': forms.TextInput,
        }


class RecipientForm(ModelForm):

    class Meta:
        model = Recipient
        fields = ['name']
        widgets = {
            'name': forms.TextInput,
        }


class RevisionForm(ModelForm):

    class Meta:
        model = Revision
        fields = ['document', 'number', 'date', 'reason']


class TimeForm(ModelForm):

    class Meta:
        model = Times
        fields = ['month', 'week']


class ProcedureForm(ModelForm):

    class Meta:
        model = Procedure
        fields = ['name', 'owner', 'process', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'process': SelectMultiple(attrs={'class': 'form-control'}),
            'owner': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control',
                 'rows': '4'}),
        }


class ActivityForm(ModelForm):

    class Meta:
        model = Activity
        fields = ['procedure', 'order', 'activity', 'owner',
            'documents', 'when_distribute']


class ActivityForm2(forms.Form):
    PROCEDURES = Procedure.objects.all()
    procedure = forms.ChoiceField(widget=forms.Select, choices=PROCEDURES)
    order = forms.IntegerField(min_value=1)
    activity = forms.CharField(widget=forms.Textarea)
    OWNERS = Agent.objects.all()
    owner = forms.ChoiceField(widget=forms.Select, choices=OWNERS)
    DOCUMENTS = Document.objects.all()
    document = forms.ChoiceField(widget=forms.Select, choices=DOCUMENTS)
    WHEN = Times.objects.all()
    when_distribute = forms.ChoiceField(widget=forms.Select, choices=WHEN)