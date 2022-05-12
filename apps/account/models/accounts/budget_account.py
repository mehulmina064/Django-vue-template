from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account


class BudgetAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    budget_amount = models.DecimalField(max_digits=15, decimal_place=2)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='budget_account_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='budget_account_modified_by')

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "Budget_account"
