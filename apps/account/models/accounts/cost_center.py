from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company

class CostCenter(models.Model):
    cost_center_name = models.CharField(max_length=200, blank=True, null=True)
    cost_center_number = models.CharField(max_length=200, blank=True, null=True)
    # parent_cost_center = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    lft = models.IntegerField()
    rgt = models.IntegerField()
    # old_parent = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='cost_center_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='cost_center_modified_by')

    def __str__(self):
        return self.cost_center_name

    class Meta:
        verbose_name_plural = "Cost_Center"
