from django.db import models
from .activitytype import ActivityType



class ActivityCost(models.Model):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    billing_rate = models.DecimalField(max_digits=10, decimal_places=2)
    costing_rate = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    