from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .bank_account import DocType


class BankTransactionPayments(models.Model):
    payment_document = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    allocated_amount = models.DecimalField(max_digits=15, decimal_place=2)
    clearance_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_transaction_payments_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_transaction_payments_modified_by')

    def __str__(self):
        return self.allocated_amount

    class Meta:
        verbose_name_plural = "Bank_Transaction_Payments"
