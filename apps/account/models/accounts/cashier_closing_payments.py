from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from .mode_of_payment import ModeOfPayment


class CashierClosingPayments(models.Model):
    # mode_of_payment = models.ForeignKey(ModeOfPayment, on_delete=CASCADE, blank=True, null=True)
    amount = models.FloatField()
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cashier_closing_payments_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cashier_closing_payments_modified_by')

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name_plural = "Cashier_Closing_Payments"

#modeofpayment-fk
