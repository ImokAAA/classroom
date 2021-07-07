from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import StudentSignUpForm
from ..models import User

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'
    success_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #user = form.save()
        return super().form_valid(form)