from django.db import models
from .activitytype import ActivityType
from .project import Project
from .task import Task


class TimesheetDetail(models.Model):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    description = models.TextField()
    expected_hours = models.FloatField()
    to_time = models.DateTimeField()
    hours = models.FloatField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_billable = models.BooleanField(default=False)
    # sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)
    billing_hours = models.FloatField()
    billing_rate = models.FloatField()
    billing_amount = models.FloatField(default=0)
    costing_rate = models.FloatField()
    costing_amount = models.FloatField(default=0)
    project_name = models.CharField(max_length=255)
    base_billing_rate = models.FloatField()
    base_billing_amount = models.FloatField()
    base_costing_rate = models.FloatField()
    base_costing_amount = models.FloatField()

    class Meta:
        db_table = 'timesheet_detail'

