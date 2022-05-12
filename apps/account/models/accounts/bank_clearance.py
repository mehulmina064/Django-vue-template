from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account
from .bank_account import BankAccount
# from .currency import Currency


class BankClearance(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE)
    # account_currency = models.ForeignKey(Currency, on_delete=CASCADE)
    from_date = models.DateField()
    bank_account = models.ForeignKey(BankAccount, on_delete=CASCADE)
    total_amount = models.IntegerField(max_length=100)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bank_clearence_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bankclrearance_modified_by')

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "BankClearance"

# Currency-FK