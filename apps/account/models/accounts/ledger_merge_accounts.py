from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .ledger_merge import LedgerMerge
from .account import Account

class LedgerMergeAccounts(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    account_name = models.CharField(max_length=150, blank=True)
    ledger_merge = models.ForeignKey(LedgerMerge, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='ledger_merge_accounts_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name='ledger_merge_accounts_modified_by')
    
    
    def __str__(self):
        return self.account
    
    class Meta:
        verbose_name_plural = "LedgerMergeAccounts"