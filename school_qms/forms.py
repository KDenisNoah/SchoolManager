from django.forms import ModelForm, TextInput, CheckboxSelectMultiple
from django import forms
from school_qms.models import *


class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ['name', 'code', 'description', 'procedure', 'code', 'record',
            'enabled', 'disabled_date', 'creation_date', 'aprobation_date',
            'document_file', 'document_url', 'owner', 'recipients',
             'when_distribute']
        widgets = {
            'name': forms.TextInput,
            'code': TextInput,
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
        fields = ['name', 'description', 'owner']
        widgets = {
            'name': forms.TextInput,
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