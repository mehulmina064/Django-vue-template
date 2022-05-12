from django.db import models
from apps.account.models.accounts.company import Company
from .project_type import ProjectType
from .project_template import ProjectTemplate


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    project_template = models.ForeignKey(ProjectTemplate, on_delete=models.CASCADE)
    expected_start_date = models.DateField()
    # after import 
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    copied_from = models.CharField(max_length=255)
    notes = models.TextField()
    actual_start_date = models.DateField()
    actual_time = models.FloatField()
    actual_end_date = models.DateField()
    estimated_costing = models.FloatField()
    total_costing_amount = models.FloatField()
    total_expense_claim = models.FloatField()
    total_purchase_cost = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    total_sales_amount = models.FloatField()
    total_billable_amount = models.FloatField()
    total_billed_amount = models.FloatField()
    total_consumed_material_cost = models.FloatField()
    # cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    gross_margin = models.FloatField()
    per_gross_margin = models.FloatField()
    # holiday_list = models.ForeignKey(HolidayList, on_delete=models.CASCADE)
    from_time = models.TimeField()
    to_time = models.TimeField()
    first_email = models.TimeField()
    second_email = models.TimeField()
    daily_time_to_send = models.TimeField()
    weekly_time_to_send = models.TimeField()
    message = models.TextField()
    priority = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    quick_entry = models.BooleanField(default=True)
    search_fields = models.CharField(max_length=255)
    show_name_in_global_search = models.BooleanField(default=True)
    sort_field = models.CharField(max_length=255)
    sort_order = models.CharField(max_length=255)
    timeline_field = models.CharField(max_length=255)
    title_field = models.CharField(max_length=255)
    track_seen = models.BooleanField(default=True)
    def __str__(self):
        return self.project_name
    
    
    
    
    
    
    
      
