from classroom.models import Auditory, Task
from django import forms

class AuditoryAddStudentForm(forms.Form):
    student_email = forms.EmailField()


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'max_grade', 'date_finish']
        widgets = {
            'date_finish': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        }