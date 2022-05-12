from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account
from .cost_center import CostCenter
from .bank_account import DocType, BankAccount
from .currency import Currency
# from .psoaproject import Project


class JournalEntryAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    account_type = models.CharField(max_length=150)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    cost_center = models.ForeignKey(CostCenter, on_delete=CASCADE, blank=True, null=True)
    party_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    party_balance = models.DecimalField(max_digits=20, decimal_places=2)
    account_currency = models.ForeignKey(Currency, on_delete=CASCADE, blank=True, null=True)
    exchange_rate = models.FloatField()
    debit_in_account_currency = models.DecimalField(max_digits=20, decimal_places=2)
    debit = models.DecimalField(max_digits=20, decimal_places=2)
    credit_in_account_currency = models.DecimalField(max_digits=20, decimal_places=2)
    credit = models.DecimalField(max_digits=20, decimal_places=2)
    # project = models.ForeignKey(Project, on_delete=CASCADE, blank=True, null=True)
    user_remark = models.TextField()
    against_account = models.TextField()
    bank_account = models.ForeignKey(BankAccount, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='journal_entry_account_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='journal_entry_account_modified_by')

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "Journal_Entry_Account"

#project-fk