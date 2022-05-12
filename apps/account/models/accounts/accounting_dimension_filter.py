from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company

class AccountDimensionFilter(models.Model):
    Company = models.ForeignKey(Company, on_delete=CASCADE)

    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_dimension_category_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='account_dimension_category_modified_by')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Account_Dimensions"

