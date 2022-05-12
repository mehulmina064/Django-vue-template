from django.db import models
from .task import Task

class TaskDependsOn(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subject = models.TextField()
    project = models.TextField()

    class Meta:
        db_table = 'tabTask Depends On'
        verbose_name = 'Task Depends On'
        verbose_name_plural = 'Task Depends On'

    def __str__(self):
        return self.subject

