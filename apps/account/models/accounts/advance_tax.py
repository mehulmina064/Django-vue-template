from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from .bank_account import DocType
from .account import Account


class AdvanceTax(models.Model):
    reference_type = models.ForeignKey(DocType, on_delete=CASCADE)
    reference_detail = models.CharField(max_length=200)
    account_head = models.ForeignKey(Account, on_delete=CASCADE)
    # allocated_amount = models.ForeignKey(partyaccountcurrency, on_delete=CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advancetax_category_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='advancetax_category_modified_by')

    def __str__(self):
        return self.allocated_amount

    class Meta:
        verbose_name_plural = "AdvanceTax"


#partyaccountcurrency-FK
