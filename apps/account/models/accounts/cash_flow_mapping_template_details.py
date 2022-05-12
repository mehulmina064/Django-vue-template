from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .cash_flow_mapping import CashFlowMapping


class CashFlowMappingTemplateDetails(models.Model):
    mapping = models.ForeignKey(CashFlowMapping, on_delete=CASCADE, blank=True, null=True)

    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cash_flow_mapping_template_details_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cash_flow_mapping_template_details_modified_by')

    def __str__(self):
        return self.mapping

    class Meta:
        verbose_name_plural = "Cash_Flow_Mapping_Template_Details"
