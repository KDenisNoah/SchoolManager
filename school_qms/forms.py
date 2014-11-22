from django.forms import ModelForm, TextInput
from django import forms
from school_qms.models import Document, Agent, Revision


class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ['name', 'code', 'description', 'procedure', 'code', 'record',
            'enabled', 'disabled_date', 'creation_date', 'aprobation_date',
            'document_file', 'document_url', 'onwer']
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


class RevisionForm(ModelForm):

    class Meta:
        model = Revision
        fields = ['document', 'number', 'date', 'reason']