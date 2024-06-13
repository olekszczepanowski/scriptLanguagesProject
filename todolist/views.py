from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from todolist.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TaskForm

class TasksList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todolist/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_completed=False).count()
        return context


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_details'
    template_name = 'todolist/task_details.html'


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('tasks')
    form_class = TaskForm


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'


class CustomLoginView(LoginView):
    template_name = "todolist/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = "todolist/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
