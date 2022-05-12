from django.db import models

class ActivityType(models.Model):
    activity_type = models.CharField(max_length=255)
    costing_rate = models.DecimalField(max_digits=19, decimal_places=2)
    billing_rate = models.DecimalField(max_digits=19, decimal_places=2)
    disabled = models.BooleanField(default=False)
   
    # objects
    objects = models.Manager()
    # permissions
    class Meta:
        permissions = (
            ('view_activity_type', 'Can view activity_type'),
            ('add_activity_type', 'Can add activity_type'),
            ('change_activity_type', 'Can change activity_type'),
            ('delete_activity_type', 'Can delete activity_type'),
        )
    # __str__
    def __str__(self):
        return self.activity_type