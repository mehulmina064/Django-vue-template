from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class CashierClosing(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    Today = models.DateField(auto_now=True)
    from_time = models.TimeField(auto_now=True)
    time = models.TimeField(auto_now=True)
    expense = models.FloatField()
    custody = models.FloatField()
    returns = models.FloatField()
    outstanding_amount = models.FloatField()
    net_amount = models.FloatField()
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cashier_closing_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cashier_closing_modified_by')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Cashier_Closing"
