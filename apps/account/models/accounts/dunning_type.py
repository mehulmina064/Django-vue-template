from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class DunningType(models.Model):
    dunning_type = models.CharField(max_length=200, blank=True, null=True)
    dunning_fee = models.DecimalField(max_digits=20, decimal_places=2)
    start_day = models.IntegerField()
    rate_of_interest = models.FloatField()
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='dunning_type_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='dunning_type_modified_by')

    def __str__(self):
        return self.dunning_type

    class Meta:
        verbose_name_plural = "dunning_type"
