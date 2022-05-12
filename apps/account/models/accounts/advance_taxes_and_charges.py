from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from .cost_center import CostCenter
from .account import Account


class AdvanceTaxAndCharges(models.Model):
    row_id = models.CharField(max_length=200)
    account_head = models.ForeignKey(Account, on_delete=CASCADE)
    description = models.TextField()
    Company = models.ForeignKey(CostCenter, on_delete=CASCADE)
    rate = models.FloatField()
    tax_amount = models.DecimalField(max_digits=20)

    def __str__(self):
        return self.row_id

    class Meta:
        verbose_name_plural = "AdvanceTaxAndCharges"

#CostCenter-Fk Company
