from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .bank_account import BankAccount
from .company import Company
# from .currency import Currency
from .bank_account import BankAccount
from .bank_account import DocType


class BankTransaction(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    # currency = models.ForeignKey(Currency, on_delete=CASCADE, blank=True, null=True)
    description = models.TextField()
    reference_number = models.CharField(max_length=200, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    allocated_amount = models.DecimalField(max_digits=15, decimal_place=2)
    # amended_from = models.ForeignKey("self")
    unallocated_amount = models.DecimalField(max_digits=15, decimal_place=2)
    party_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    deposit = models.DecimalField(max_digits=15, decimal_place=2)
    withdrawal = models.DecimalField(max_digits=15, decimal_place=2)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_transaction_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_transaction_modified_by')

    def __str__(self):
        return self.bank_account

    class Meta:
        verbose_name_plural = "Bank_Transaction"

# company-FK
# currency-FK
