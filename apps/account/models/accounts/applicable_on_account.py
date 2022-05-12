from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account


class ApplicableOnAccount(models.Model):
    applicable_on_account = models.ForeignKey(Account, on_delete=CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='applicable_on_account_dimension_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='applicable_on_account_modified_by')

    def __str__(self):
        return self.applicable_on_account

    class Meta:
        verbose_name_plural = "Applicable_On_Account"
