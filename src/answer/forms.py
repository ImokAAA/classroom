from django import forms
from django.db.models import fields

from .models import Answer

class AnswerAssignForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['grade'] 