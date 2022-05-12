from django.db import models
from django.contrib.auth.models import User
from apps.account.models.accounts.company import Company
from .project import Project
from apps.account.models.accounts.currency import Currency


class TimeSheet(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    #  after add this model
    # sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)
    # salary_slip = models.ForeignKey(SalarySlip, on_delete=models.CASCADE)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_hours = models.FloatField()
    total_billable_hours = models.FloatField()
    total_billed_hours = models.FloatField()
    total_costing_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_billable_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_billed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    per_billed = models.FloatField()
    note = models.TextField()
    parent_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    base_total_costing_amount = models.DecimalField(max_digits=10, decimal_places=2)
    base_total_billable_amount = models.DecimalField(max_digits=10, decimal_places=2)
    base_total_billed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)

    