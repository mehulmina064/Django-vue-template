from django.contrib import admin

# Register your models here.
from apps.projectmanagement import models 

admin.site.register(models.ActivityCost)
admin.site.register(models.ActivityType)
admin.site.register(models.DependentTask)
admin.site.register(models.ProjectTemplateTask)
admin.site.register(models.ProjectTemplate)
admin.site.register(models.ProjectType)
admin.site.register(models.ProjectUpdate)
admin.site.register(models.ProjectUser)
admin.site.register(models.Project)
admin.site.register(models.TaskDependsOn)
admin.site.register(models.TaskType)
admin.site.register(models.Task)
admin.site.register(models.TimesheetDetail)
admin.site.register(models.TimeSheet)

