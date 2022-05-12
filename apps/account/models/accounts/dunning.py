from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from .company import Company
# from .dunningtype import DunningType
# from .salesinvoice import SalesInvoice
from .currency import Currency
# from ..selling.customer import Customer


class Language:
    pass


class Dunning(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    # sales_invoice = models.ForeignKey(SalesInvoice, on_delete=CASCADE, blank=True, null=True)
    customer_name = models.CharField(max_length=150, blank=True, null=True)
    outstanding_amount = models.DecimalField(max_digits=15, decimal_places=2)
    posting_date = models.DateField(auto_now_add=True)
    # dunning_type = models.ForeignKey(DunningType, on_delete=CASCADE, blank=True, null=True)
    interest_amount = models.DecimalField(max_digits=15, decimal_places=2)
    dunning_fee = models.DecimalField(max_digits=15, decimal_places=2)
    language = models.ForeignKey(Language, on_delete=CASCADE, blank=True, null=True)
    # letter_head = models.ForeignKey(LetterHead, on_delete=CASCADE, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=CASCADE, blank=True, null=True)
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    due_date = models.DateField(auto_now_add=True)
    posting_time = models.TimeField(auto_now_add=True)
    address_display = models.TextField()
    contact_mobile = models.IntegerField()
    company_address_display = models.TextField()
    contact_email = models.EmailField()
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    Currency = models.DecimalField(max_digits=15, decimal_places=2)
    dunning_amount = models.DecimalField(max_digits=15, decimal_places=2)
    conversion_rate = models.FloatField()
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='distributed_cost_center_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='distributed_cost_center_modified_by')

    def __str__(self):
        return self.cost_center

    class Meta:
        verbose_name_plural = "Distributed_Cost_Center"

#salesinvoice-fk
#dunning type-fk
#customer-fk
#letterhead-fk