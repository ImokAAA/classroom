from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

from classroom.models import Task
from users.models import Student

from datetime import datetime
class Answer(models.Model):
    '''
    Defines student answer to the task
    '''
    task = ForeignKey(Task, on_delete=models.CASCADE)
    student = OneToOneField(Student, on_delete=models.CASCADE)
    description = TextField()
    date_submit = DateTimeField(auto_now_add=True)
    grade = IntegerField(blank = True, null=True)
    date_assigned = DateTimeField(blank = True, null=True)

    def is_assigned(self):
        if self.date_assigned:
            return True
        return False

    def answer_assign(self, grade):
        self.grade = grade
        self.date_assigned = datetime.now()
        self.save()

    def is_match_max_grade(self, grade):
        if grade <= self.task.max_grade:
            return True
        return False    

    
