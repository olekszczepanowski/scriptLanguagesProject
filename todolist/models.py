from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    TECHNOLOGY_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('css', 'CSS'),
        ('html', 'HTML'),
        ('cpp', 'C++'),
        ('c', 'C'),
        ('docker', 'Docker'),
        ('git', 'Git'),
        ('react', 'React'),
        ('django', 'Django'),
        ('php', 'PHP'),
        ('java', 'Java'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    technology = models.CharField(max_length=10, choices=TECHNOLOGY_CHOICES, default='Other')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_completed', 'created_at']
