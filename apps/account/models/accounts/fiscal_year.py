from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from .company import Company


class FiscalYear(models.Model):
    year = models.CharField(max_length=200, blank=True, null=True)
    year_start_date = models.DateField(auto_now_add=True)
    year_end_date = models.DateField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='fiscal_year_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='fiscal_year_modified_by')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name_plural = "Fiscal_Year"


class FiscalYearCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return self.company
