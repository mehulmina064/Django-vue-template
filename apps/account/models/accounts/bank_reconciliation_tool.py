from django.db import models
from django.db.models import DecimalField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
from .bank_account import BankAccount


class BankReconciliationTool(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=CASCADE, blank=True, null=True)
    bank_statement_from_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    bank_statement_to_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    account_opening_balance = models.DecimalField(max_digits=15, decimal_places=2)
    bank_statement_closing_balance = DecimalField(max_digits=15, decimal_places=2)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_reconciliation_tool_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_reconciliation_tool_modified_by')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Bank_Reconciliation_Tool"

# company-FK