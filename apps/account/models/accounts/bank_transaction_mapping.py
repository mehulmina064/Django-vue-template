from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class BankTransactionMapping(models.Model):
    file_field = models.CharField(max_length=200, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_transaction_mapping_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_transaction_mapping_modified_by')

    def __str__(self):
        return self.file_field

    class Meta:
        verbose_name_plural = "Bank_Transaction_Mapping"
