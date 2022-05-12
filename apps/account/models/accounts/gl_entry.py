from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account
from .bank_account import DocType
from .cost_center import CostCenter
from .currency import Currency
from .finance_book import FinanceBook
from .company import Company
from .fiscal_year import FiscalYear
# from .psoa_project import Project


class GlEntry(models.Model):
    posting_date = models.DateField(auto_now_add=True)
    transaction_date = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    party_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    cost_center = models.ForeignKey(CostCenter, on_delete=CASCADE, blank=True, null=True)
    debit = models.DecimalField(max_digits=20, decimal_places=2)
    account_currency = models.ForeignKey(Currency, on_delete=CASCADE, blank=True, null=True)
    debit_in_account_currency = models.DecimalField(max_digits=20, decimal_places=2)
    credit_in_account_currency = models.DecimalField(max_digits=20, decimal_places=2)
    against = models.TextField()
    against_voucher_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    voucher_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    voucher_detail_no = models.CharField(max_length=200, blank=True)
    # project = models.ForeignKey(Project, on_delete=CASCADE, blank=True, null=True)
    remarks = models.TextField()
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    finance_book = models.ForeignKey(FinanceBook, on_delete=CASCADE, blank=True, null=True)
    due_date = models.DateField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='gl_entry_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='gl_entry_modified_by')

    def __str__(self):
        return self.transaction_date

    class Meta:
        verbose_name_plural = "Gl_Entry"

#project-FK