from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from apps.inventory.models.accounts.bank_account import DocType
# from .bankaccount import DocType


class AllowedDimension(models.Model):
    accounting_dimension = models.ForeignKey(DocType, on_delete=CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allowed_dimension_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='allowed_dimension_modified_by')

    def __str__(self):
        return self.accounting_dimension

    class Meta:
        verbose_name_plural = "Allowed_Dimension"
