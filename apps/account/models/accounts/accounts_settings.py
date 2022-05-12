from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User



class AccountSettings(models.Model):
    acc_frozen_upto = models.DateField()
    # frozen_accounts_modifier = models.ForeignKey(Role, on_delete=CASCADE)
    # credit_controller = models.ForeignKey(Role, on_delete=CASCADE)
    stale_days = models.IntegerField(max_length=100)
    # over_billing_allowance = models.ForeignKey(Currency, on_delete=CASCADE)
    # role_allowed_to_over_bill = models.ForeignKey(Role, on_delete=CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_setting_category_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='account_setting_category_modified_by')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Accounting_Dimension"


# Dependency
# Role-FK
# Currency-FK