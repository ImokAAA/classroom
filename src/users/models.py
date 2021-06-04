from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, CharField

class User(AbstractUser):
    #username = None
    email = models.EmailField(unique=True)
    #name = CharField(max_length=150, blank=True)
    #surname = CharField(max_length=150, blank = True)
    is_student = BooleanField(default=False)
    is_teacher = BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)
