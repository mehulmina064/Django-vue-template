from django.db import models

class ProjectType(models.Model):
    project_type = models.CharField(max_length=255)
    description = models.TextField()
    creation = models.DateTimeField()
    modified = models.DateTimeField()
    modified_by = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    allow_copy = models.BooleanField()
    allow_guest_to_view = models.BooleanField()
    allow_import = models.BooleanField()
    allow_rename = models.BooleanField()
    autoname = models.CharField(max_length=255)
    beta = models.BooleanField()
    custom = models.BooleanField()
    docstatus = models.IntegerField()
    doctype = models.CharField(max_length=255)
    document_type = models.CharField(max_length=255)
    editable_grid = models.BooleanField()
    engine = models.CharField(max_length=255)
    has_web_view = models.BooleanField()
    hide_heading = models.BooleanField()
    hide_toolbar = models.BooleanField()
    idx = models.IntegerField()
    image_view = models.BooleanField()
    in_create = models.BooleanField()
    is_submittable = models.BooleanField()
    issingle = models.BooleanField()
    is_table = models.BooleanField()
    max_attachments = models.IntegerField()
    module = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name_case = models.CharField(max_length=255)
    quick_entry = models.BooleanField()
    read_only = models.BooleanField()
    read_only_onload = models.BooleanField()
    show_name_in_global_search = models.BooleanField()
    sort_field = models.CharField(max_length=255)
    sort_order = models.CharField(max_length=255)
    track_changes = models.BooleanField()
    track_seen = models.BooleanField()