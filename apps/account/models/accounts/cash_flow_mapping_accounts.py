from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account


class CashFlowMappingAccounts(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cash_flow_mapping_accounts_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cash_flow_mapping_accounts_modified_by')

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "Cash_Flow_Mapping_Accounts"
