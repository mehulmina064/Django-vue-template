from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Bank(models.Model):
    bank_name = models.CharField(max_length=200)
    swift_number = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    plaid_access_token = models.CharField(max_length=200)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='applicable_on_account_dimension_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='applicable_on_account_modified_by')

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name_plural = "Bank"
