from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class CashFlowMapping(models.Model):
    mapping_name = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=100, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cash_flow_mapping_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cash_flow_mapping_modified_by')

    def __str__(self):
        return self.mapping_name

    class Meta:
        verbose_name_plural = "Cash_Flow_Mapping"
