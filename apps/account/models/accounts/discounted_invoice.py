from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from inventory.management.accounts.salesinvoice import SalesInvoice

from .account import Account
# from ..selling.customer import Customer


class DiscountedInvoice(models.Model):
    # sales_invoice = models.ForeignKey(SalesInvoice, on_delete=CASCADE, blank=True, null=True)
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    posting_date = models.DateField(auto_now_add=True)
    outstanding_amount = models.DecimalField(max_digits=24, decimal_places=2)
    debit_to = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='customer_group_item_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='customer_group_item_modified_by')

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name_plural = "Customer_Item"

#salesinvoice -fk
#customer-fk
