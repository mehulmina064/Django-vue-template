from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .bank_account_subtype import BankAccountSubtype
from .bank_account_type import BankAccountType
from .account import Account
from .bank import Bank
from .company import Company

class DocType(models.Model):
    Doc_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Doc_type


class BankAccount(models.Model):
    account_name = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=CASCADE)
    bank = models.ForeignKey(Bank, on_delete=CASCADE)
    account_type=models.ForeignKey(BankAccountType,on_delete=CASCADE)
    account_subtype = models.ForeignKey(BankAccountSubtype, on_delete=CASCADE)
    company = models.ForeignKey(Company, on_delete=CASCADE)
    party_type = models.ForeignKey(DocType, on_delete=CASCADE)
    iban = models.CharField(max_length=30)
    bank_account_no = models.IntegerField(max_length=100)
    integration_id = models.IntegerField(max_length=100)
    last_integration_date = models.DateField()
    mask = models.CharField(max_length=200)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bankaccount_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bankaccount_modified_by')
    address_and_contact = models.CharField(max_length=200, blank=True,related_name='Address_And_Contact')
    branch_code = models.CharField(max_length=200, blank=True,   related_name='Branch_Code')



    def __str__(self):
        return self.account_name

    class Meta:
        verbose_name_plural = "BankAccount"

#Company-FK