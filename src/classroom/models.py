from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from users.models import Student, Teacher, User


class Auditory(models.Model):
    ''' 
    Defines groups of students that teacher organizes.
    '''
    name = CharField(max_length=150)
    description = TextField(blank = True, null=True)
    teacher = ManyToManyField(Teacher)
    student = ManyToManyField(Student)

    def add_teacher_object(self, user):
        teacher_object = Teacher.objects.get(user=user)
        auditory = self.teacher.add(teacher_object)


    def add_student_with_email(self, email):
        user = User.objects.get(email = email)
        student_object = Student.objects.get(user = user)
        auditory = self.student.add(student_object)


    def techer_email(self):
        return [teacher.email for teacher in self.teacher.all()]

    def student_email(self):
        if self.student.all():
            return self.student.email
        return 'No student yet in this auditory'


class Task(models.Model):
    '''
    Defines tasks wich teacher can give to class or specific students.
    '''
    name = CharField(max_length=150)
    description = TextField(blank = True, null=True)
    auditory = ManyToManyField(Auditory)
    teacher = ForeignKey(Teacher, on_delete = models.CASCADE)
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
    
