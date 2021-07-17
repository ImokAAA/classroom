from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ManyToManyField, OneToOneField
from users.models import Student, Teacher


class Auditory(models.Model):
    ''' 
    Defines groups of students that teacher organizes.
    '''
    name = CharField(max_length=150)
    description = TextField(blank = True, null=True)
    teacher = ManyToManyField(Teacher)
    student = ManyToManyField(Student)


class Task(models.Model):
    '''
    Defines tasks wich teacher can give to class or specific students.
    '''
    name = CharField(max_length=150)
    description = TextField(blank = True, null=True)
    auditory = ManyToManyField(Auditory)
    teacher = OneToOneField(Teacher, on_delete = models.CASCADE)
    max_grade = IntegerField()
    date_start = DateTimeField(auto_now_add=True)
    date_finish = DateTimeField()


class Assignment(models.Model):
    '''
    Defines assignments which are needed to check tasks.
    '''
    task = OneToOneField(Task, on_delete=models.CASCADE)
    teacher = OneToOneField(Teacher, on_delete=models.CASCADE)
    student = OneToOneField(Student, on_delete=models.CASCADE)
    grade = IntegerField()
    date_assigned = DateTimeField(auto_now_add=True)
    
