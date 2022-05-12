from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account
from .bank_account import DocType
from .currency import Currency


class ExchangeRateRevaluationAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    party_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    account_currency = models.ForeignKey(Currency, on_delete=CASCADE, blank=True, null=True)
    balance_in_account_currency = models.DecimalField(max_digits=20, decimal_places=2)
    current_exchange_rate = models.FloatField()
    balance_in_base_currency = models.FloatField()
    new_exchange_rate = models.FloatField()
    new_balance_in_base_currency = models.FloatField()
    gain_loss = models.DecimalField(max_digits=20, decimal_places=2)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='exchange_rate_revaluation_account_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='exchange_rate_revaluation_account_modified_by')

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "Exchange_Rate_Revaluation_Account"
