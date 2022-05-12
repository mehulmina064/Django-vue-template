from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Campaign"


class CampaignItem(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='campaign_item_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='campaign_item_modified_by')

    def __str__(self):
        return self.campaign

    class Meta:
        verbose_name_plural = "Campaign_Items"
