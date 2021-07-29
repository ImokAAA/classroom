from django.db.models import fields
from classroom.models import Auditory
from django import forms

class AuditoryAddStudentForm(forms.Form):
    student_email = forms.EmailField()


