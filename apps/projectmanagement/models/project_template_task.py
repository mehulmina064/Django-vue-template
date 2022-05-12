from django.db import models
from django.contrib.auth.models import User
from .task import Task

class ProjectTemplateTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    creation = models.DateTimeField()
    modified = models.DateTimeField()
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # after add
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sort_field = models.CharField(max_length=255)
    sort_order = models.CharField(max_length=255)
    track_changes = models.BooleanField()
    is_table = models.BooleanField()
    quick_entry = models.BooleanField()
    editable_grid = models.BooleanField()
    engine = models.CharField(max_length=255)
    doctype = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    # permissions = models.ManyToManyField(Permission)
    # actions = models.ManyToManyField(Action)
    # links = models.ManyToManyField(Link)
    # fields = models.ManyToManyField(Field)
    # field_order = models.ManyToManyField(FieldOrder)
