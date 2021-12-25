from django.forms.models import modelformset_factory
from django import forms
from .models import *


class QuestionsForm(forms.ModelForm):
    text = forms.CharField(label='Question', required=True)
    
    class Meta:
        model = Question
        fields = ['text']


AnswerFormset = modelformset_factory(
    Answer,
    fields=('text', 'correct'),
    extra=4,
    widgets={ 'text': forms.TextInput(attrs={ 'class': 'form-control','placeholder': 'Enter Answer here'}
            )
        }
)        

