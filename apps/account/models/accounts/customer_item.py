from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# from inventory.management.selling.customer import Customer


class CustomerItem(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='customer_group_item_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='customer_group_item_modified_by')

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name_plural = "Customer_Item"


# from selling customer-fk