from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company


class ExchangeRateRevaluation(models.Model):
    posting_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    total_gain_loss = models.DecimalField(max_digits=20, decimal_places=2)
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='exchange_rate_revaluation_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='exchange_rate_revaluation_modified_by')

    def __str__(self):
        return self.dunning_type

    class Meta:
        verbose_name_plural = "dunning_type"
