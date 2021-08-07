from answer.forms import AnswerAssignForm
from users.models import Student
from answer.models import Answer 
from classroom.models import Auditory, Task

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

class AnswerSubmitView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = 'answer/answer_submit.html'
    fields = ['description']

    def get_context_data(self, **kwargs):
        self.task = get_object_or_404(Task, pk = self.kwargs['pk'])
        self.auditory = get_object_or_404(Auditory, pk = self.kwargs['auditory_pk'])

        data = super().get_context_data(**kwargs)
        data.update({'task': self.task, 'auditory': self.auditory})
        return data

    def form_valid(self, form):
        self.student = get_object_or_404(Student, user = self.request.user)
        form.instance.student = self.student
        self.task = get_object_or_404(Task, pk = self.kwargs['pk'])
        form.instance.task = self.task
    
        self.object = form.save()
        self.auditory = get_object_or_404(Auditory, pk = self.kwargs['auditory_pk'])
        return HttpResponseRedirect(reverse('classroom:task-list', args=(self.auditory.id,)))
        
        
class AnswerListForTaskView(LoginRequiredMixin, ListView):
    model = Answer
    template_name = 'answer/answer_list_for_task.html'
    context_object_name = 'answers'

    def get(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk = self.kwargs['pk'])
        self.object_list = Answer.objects.filter(task = self.task).order_by('-date_submit')
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        self.task = get_object_or_404(Task, pk = self.kwargs['pk'])
        self.auditory = get_object_or_404(Auditory, pk = self.kwargs['auditory_pk'])
        data = super().get_context_data(**kwargs)
        data.update({'task': self.task, 'auditory': self.auditory})
        return data


class AnswerDetailView(LoginRequiredMixin, DetailView):
    model = Answer
    slug_field = 'id'
    template_name = 'answer/answer_detail.html'
    context_object_name = 'answer'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        self.auditory = get_object_or_404(Auditory, pk = self.kwargs['auditory_pk'])
        data = super().get_context_data(**kwargs)
        data.update({'auditory': self.auditory})
        return data


class AnswerAssignView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = AnswerAssignForm()
        self.auditory = get_object_or_404(Auditory, pk = self.kwargs['auditory_pk'])
        self.answer = get_object_or_404(Answer, pk = self.kwargs['pk'])
        return render(request,
        'answer/answer_assign.html',
        {'form': form, 'auditory' : self.auditory, 'max_grade': self.answer.task.max_grade} 
        )

    def post(self, request, *args, **kwargs):
        form = AnswerAssignForm(request.POST)
        self.answer = get_object_or_404(Answer, pk = self.kwargs['pk'])
        self.auditory = get_object_or_404(Auditory, pk = self.kwargs['auditory_pk'])
        if form.is_valid():
            if self.answer.is_match_max_grade(form.cleaned_data['grade']):
                self.answer.answer_assign(form.cleaned_data['grade'])
                return HttpResponseRedirect(reverse('answer:detail', args=(self.answer.id, self.auditory.id))) 
            return HttpResponseBadRequest('Grade should be greater than maximum grade')
        raise HttpResponseBadRequest('form is not valid')


