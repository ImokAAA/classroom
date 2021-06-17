from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db import transaction

from users.models import Teacher, Student, User

class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {'email': UsernameField}

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {'email': UsernameField}

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user