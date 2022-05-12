from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class BankAccountSubtype(models.Model):
    account_subtype = models.CharField(max_length=200)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_account_subtype_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_account_subtype_modified_by')

    def __str__(self):
        return self.account_subtype

    class Meta:
        verbose_name_plural = "Bank_Account_Type"
