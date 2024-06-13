from django.urls import path
from .views import TasksList, TaskDetails, CreateTask, UpdateTask, DeleteTask, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path("", TasksList.as_view(), name="tasks"),
    path("task/<int:pk>", TaskDetails.as_view(), name="task"),
    path("task-create/", CreateTask.as_view(), name="task-create"),
    path("task-update/<int:pk>", UpdateTask.as_view(), name="task-update"),
    path("task-delete/<int:pk>", DeleteTask.as_view(), name="task-delete"),
]
