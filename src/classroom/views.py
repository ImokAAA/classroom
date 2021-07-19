from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Auditory, Task, Assignment

class AuditoryListView(LoginRequiredMixin, ListView):   
    model = Auditory
    template_name = 'auditory/auditory_list.html'
    context_object_name = 'auditories'


class AuditoryDetailView(LoginRequiredMixin, DetailView):
    model = Auditory
    slug_field = 'id'
    template_name = 'auditory/auditory_detail.html'
    context_object_name = 'auditory'


class AuditoryCreateView(LoginRequiredMixin, CreateView):
    model = Auditory
    template_name = 'auditory/auditory_create.html'
    fields = ['name', 'description', 'teacher', 'student']
    success_url = '/classroom/list/'

class AuditoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Auditory
    success_url = '/classroom/list/'
    slug_field = 'id'
    template_name = 'auditory/auditory_confirm_delete.html'

class TaskListView(ListView):
    model = Task
    pass


class TaskDetailView(DetailView):
    model = Task
    pass


class TaskCreateView(CreateView):
    model = Task
    pass


class TaskDeleteView(DeleteView):
    model = Task
    pass


