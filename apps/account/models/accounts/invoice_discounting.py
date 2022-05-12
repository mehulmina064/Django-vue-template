from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
from .account import Account


class InvoiceDiscounting(models.Model):
    posting_date = models.DateField(auto_now_add=True)
    loan_start_date = models.DateField(auto_now_add=True)
    loan_period = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    bank_charges = models.DecimalField(max_digits=20, decimal_places=2)
    short_term_loan = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    bank_charges_account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    accounts_receivable_unpaid = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='invoice_discounting_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='invoice_discounting_modified_by')

    def __str__(self):
        return self.posting_date

    class Meta:
        verbose_name_plural = "Invoice_Discounting"
