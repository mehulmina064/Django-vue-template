from django.db import models
from django.contrib.auth.models import User
from .task import Task

class DependentTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    allow_copy = models.BooleanField(default=False)
    allow_import = models.BooleanField(default=False)
    allow_rename = models.BooleanField(default=False)
    beta = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)
    custom = models.BooleanField(default=False)
    docstatus = models.IntegerField(default=0)
    doctype = models.CharField(max_length=255, default='DocType')
    document_type = models.CharField(max_length=255, default='')
    editable_grid = models.BooleanField(default=False)
    hide_heading = models.BooleanField(default=False)
    hide_toolbar = models.BooleanField(default=False)
    idx = models.IntegerField(default=0)
    image_view = models.BooleanField(default=False)
    in_create = models.BooleanField(default=False)
    is_submittable = models.BooleanField(default=False)
    issingle = models.BooleanField(default=False)
    is_table = models.BooleanField(default=False)
    max_attachments = models.IntegerField(default=0)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.CharField(max_length=255, default='Projects')
    name = models.CharField(max_length=255, default='Dependent Task')
    name_case = models.CharField(max_length=255, default='')
    # after add
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quick_entry = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    read_only_onload = models.BooleanField(default=False)
    sort_field = models.CharField(max_length=255, default='modified')
    sort_order = models.CharField(max_length=255, default='DESC')
    track_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Dependent Task'
        verbose_name = 'Dependent Task'
        verbose_name_plural = 'Dependent Task'

