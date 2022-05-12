from django.db import models
from django.utils.translation import gettext_lazy as _
from .project import Project
from .task_type import TaskType
from apps.account.models.accounts.company import Company
from django.contrib.auth.models import User


class Task(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   # issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
   type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
   is_group = models.BooleanField(default=False)
   # parent_task = models.ForeignKey(self, on_delete=models.CASCADE, null=True, blank=True)
   exp_start_date = models.DateField(null=True, blank=True)
   expected_time = models.FloatField(null=True, blank=True)
   task_weight = models.FloatField(null=True, blank=True)
   exp_end_date = models.DateField(null=True, blank=True)
   description = models.TextField(null=True, blank=True)
   act_start_date = models.DateField(null=True, blank=True)
   actual_time = models.FloatField(null=True, blank=True)
   act_end_date = models.DateField(null=True, blank=True)
   total_costing_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   total_expense_claim = models.DecimalField(max_digits=10, decimal_places=2)
   total_billing_amount = models.DecimalField(max_digits=10, decimal_places=2)
   review_date = models.DateField()
   closing_date = models.DateField()
   # department = models.ForeignKey(Department, on_delete=models.CASCADE)
   company = models.ForeignKey(Company, on_delete=models.CASCADE)
   lft = models.IntegerField()
   rgt = models.IntegerField()
   old_parent = models.CharField(max_length=140)
   completed_by = models.ForeignKey(User, on_delete=models.CASCADE)
   is_template = models.BooleanField()
   start = models.IntegerField()
   duration = models.IntegerField()
   completed_on = models.DateField()

class Meta:
    db_table = 'task'



   
   

