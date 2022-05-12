from django.db import models

from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
from .bank import Bank
from .bank_account import BankAccount
from .bank_account import DocType


class BankStatementImport(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=CASCADE, blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=CASCADE, blank=True, null=True)
    import_file = models.FileField(upload_to='documents/%Y/%m/%d')
    google_sheets_url = models.URLField()
    reference_doctype = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_statement_import_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_statement_import_modified_by')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Bank_Statement_Import"

# company-FK