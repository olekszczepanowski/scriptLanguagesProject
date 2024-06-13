from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    completion_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'completion_date']
