from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account
from .company import Company


class LedgerMerge(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    account_name = models.CharField(max_length=150, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='ledger_merge_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='ledger_merge_modified_by')

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "LedgerMerge"


class LedgerMergeAccounts(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "LedgerMergeAccounts"
