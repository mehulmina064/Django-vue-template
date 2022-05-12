from django.db import models 
from .project_type import ProjectType

class ProjectTemplate(models.Model):
    name = models.CharField(max_length=255)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)