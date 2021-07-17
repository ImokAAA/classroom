from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from .models import Auditory, Task, Assignment

class AuditoryListView(ListView):   
    model = Auditory
    template_name = 'auditory/auditory_list.html'
    context_object_name = 'auditories'

class AuditoryDetailView(DetailView):
    model = Auditory
    slug_field = 'id'
    template_name = 'auditory_detail.html'


class AuditoryCreateView(CreateView):
    model = Auditory
    template_name = 'auditory_create.html'

class AuditoryDeleteView(DeleteView):
    model = Auditory


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


