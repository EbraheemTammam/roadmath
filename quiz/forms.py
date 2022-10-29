from dataclasses import fields
from optparse import Option
from django.forms import ModelForm
from django import forms
from .models import Question

class QestionForm(ModelForm):
    
    class Meta:
        model = Question
        fields = ('question', 'answers')
        widgets = {
            'answers': forms.RadioSelect(),
       }


#form = QForm(options=<DYNAMIC_VALUE>)