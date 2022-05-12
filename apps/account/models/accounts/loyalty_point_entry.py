from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
# from .territory_item import Territory
from .account import Account
from .bank_account import DocType
# from ..selling.customer import CustomerGroup, Customer


class LoyaltyProgram(models.Model):
    loyalty_program_name = models.CharField(max_length=150, blank=True, null=True)
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField(auto_now_add=True)
    # customer_group = models.ForeignKey(CustomerGroup, on_delete=CASCADE, blank=True, null=True)
    # customer_territory = models.ForeignKey(Territory, on_delete=CASCADE, blank=True, null=True)
    conversion_factor = models.FloatField()
    expiry_duration = models.IntegerField()
    expense_account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return self.loyalty_program_name

    class Meta:
        verbose_name_plural = "loyalty_program_name"


class LoyaltyPointEntry(models.Model):
    loyalty_program = models.ForeignKey(LoyaltyProgram, on_delete=CASCADE, blank=True, null=True)
    loyalty_program_tier = models.CharField(max_length=150, blank=True)
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    loyalty_points = models.IntegerField()
    purchase_amount = models.DecimalField(max_digits=20, decimal_places=2)
    expiry_date = models.DecimalField(max_digits=20, decimal_places=2)
    posting_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    invoice_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='loyalty_point_entry_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='loyalty_point_entry_modified_by')

    def __str__(self):
        return self.loyalty_program

    class Meta:
        verbose_name_plural = "loyalty_point_entry"


class LoyaltyPointEntryRedemption(models.Model):
    sales_invoice = models.CharField(max_length=150, blank=True, null=True)
    redemption_date = models.DateField(auto_now_add=True)
    redeemed_points = models.IntegerField()


class LoyaltyProgramCollection(models.Model):
    tier_name = models.CharField(max_length=150, blank=True, null=True)
    min_spent = models.DecimalField(max_digits=20, decimal_places=2)
    collection_factor = models.DecimalField(max_digits=20, decimal_places=2)


#customergroup-fk
#customer-fk
#territory-fk