from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# from inventory.management.selling.customer import Customer

class CouponCode(models.Model):
    coupon_name = models.CharField(max_length=200, blank=True, null=True)
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    coupon_code = models.CharField(max_length=200, blank=True, null=True)
    valid_from = models.CharField(max_length=200, blank=True, null=True)
    valid_upto = models.DateField(auto_now_add=True)
    used = models.IntegerField()
    description = models.TextField()
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='coupon_code_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='coupon_code_modified_by')

    def __str__(self):
        return self.coupon_name

    class Meta:
        verbose_name_plural = "Coupon_Code"

#customer-fk