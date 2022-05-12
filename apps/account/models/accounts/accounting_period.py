from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company

class AccountingPeriod(models.Model):
    period_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounting_period_category_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='accounting_period_category_modified_by')

    def __str__(self):
        return self.period_name

    class Meta:
        verbose_name_plural = "Accounting_Period"

# Dependency
# Company-FK  