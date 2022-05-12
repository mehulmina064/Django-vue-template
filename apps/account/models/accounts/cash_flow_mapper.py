from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class CashFlowMapper(models.Model):
    section_name = models.CharField(max_length=100, blank=True)
    section_header = models.CharField(max_length=100, blank=True)
    section_leader = models.CharField(max_length=100, blank=True)
    section_subtotal = models.CharField(max_length=100, blank=True)
    section_footer = models.CharField(max_length=100, blank=True)
    position = models.IntegerField()
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cash_flow_mapper_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cash_flow_mapper_modified_by')

    def __str__(self):
        return self.section_subtotal

    class Meta:
        verbose_name_plural = "Cash_Flow_Mapper"
