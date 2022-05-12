from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account
from .bank import Bank
from .bank_account import BankAccount
from .bank_account import DocType
# from supplier import Supplier

# from .psoaproject import Project
# from ..selling.customer import Customer


class BankGuarantee(models.Model):
    reference_doctype = models.ForeignKey(DocType, on_delete=CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    # supplier = models.ForeignKey(Supplier, on_delete=CASCADE, blank=True, null=True)
    # project = models.ForeignKey(Project, on_delete=CASCADE, blank=True, null=True)
    # currencies#
    start_date = models.DateField(auto_now_add=True, null=True, blank=True)
    validity = models.IntegerField()
    end_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=CASCADE, blank=True, null=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=CASCADE, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    bank_account_no = models.CharField(max_length=200, blank=True, null=True)
    iban = models.CharField(max_length=200, blank=True, null=True)
    branch_code = models.CharField(max_length=200, blank=True, null=True)
    swift_number = models.CharField(max_length=200, blank=True, null=True)
    bank_guarantee_number = models.IntegerField(max_length=100)
    name_of_beneficiary = models.CharField(max_length=200, blank=True, null=True)
    # margin_money =  field type currency
    # charges =
    fixed_deposit_number = models.CharField(max_length=200, blank=True, null=True)
    # amended_from = models.ForeignKey("Self")
    # modified_on = models.DateTimeField(auto_now=True)
    modified_on=models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_guarantee_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_guarantee_modified_by')

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name_plural = "Bank_Guarantee"

#customer-FK
#supplier-FK
#project-FK