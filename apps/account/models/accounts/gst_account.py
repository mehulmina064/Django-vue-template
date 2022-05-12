from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
from .account import Account


class Gstaccount(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    cgst_account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    sgst_account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='gst_account_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='gst_account_modified_by')

    def __str__(self):
        return self.cgst_account

    class Meta:
        verbose_name_plural = "Gst_account"
