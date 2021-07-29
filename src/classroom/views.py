from django.views.generic.base import View
from classroom.forms import AuditoryAddStudentForm
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
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
    fields = ['name', 'description']
    success_url = '/classroom/list/'
    
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        description = form.cleaned_data.get("description")
        auditory = Auditory.objects.create(name = name, description = description)
        auditory.add_teacher_object(self.request.user)
        return HttpResponseRedirect(self.success_url)


class AuditoryAddStudentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = AuditoryAddStudentForm()
        return render(request,
        'auditory/auditory_add_student.html',
        {'form': form} 
        )

    def post(self, request, *args, **kwargs):
        auditory = get_object_or_404(Auditory, pk = kwargs['pk'])
        form = AuditoryAddStudentForm(request.POST)
        if form.is_valid():
            auditory.add_student_with_email(form.cleaned_data['student_email'])       
            return HttpResponseRedirect(reverse('classroom:detail', args=(auditory.id,))) 

        raise HttpResponseBadRequest('form is not valid')
    


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


