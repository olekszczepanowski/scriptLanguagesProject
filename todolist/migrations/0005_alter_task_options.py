# Generated by Django 5.0.6 on 2024-06-15 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_task_technology'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_completed', 'created_at']},
        ),
    ]
