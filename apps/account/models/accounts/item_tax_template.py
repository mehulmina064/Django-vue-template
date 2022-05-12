from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
from .account import Account

class ItemTaxTemplate(models.Model):
    title = models.CharField(max_length=200, null=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='item_tax_template_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='item_tax_template_modified_by')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Item_Tax_Template"


class Item_Tax_Template_Detail(models.Model):
    tax_type = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    item_tax_template = models.ForeignKey(ItemTaxTemplate, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name='item_tax_template_detail_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name='item_tax_template_detail_modified_by')
    
    def __str__(self):
        return self.tax_type.account_name
    
