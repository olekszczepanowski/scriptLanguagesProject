from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from todolist.models import Task


class TasksList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todolist/task_list.html'


class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task_details'
    template_name = 'todolist/task_details.html'


class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class UpdateTask(UpdateView):
    model = Task
    success_url = reverse_lazy('tasks')
    fields = '__all__'


class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'

class CustomLoginView(LoginView):
    template_name = "todolist/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')
