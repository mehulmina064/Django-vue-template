from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
# from apps.organizations.models import Organization

# class Account(models.Model):
#     account_name = models.CharField(max_length=200)
#     account_number = models.IntegerField()
#     company = models.ForeignKey(Company, on_delete=CASCADE)
#    #account_currency = models.ForeignKey(Currency, on_delete=CASCADE)
#     # parent_account = models.ForeignKey("Self", on_delete=CASCADE, blank=True, null=True)
#     tax_rate = models.FloatField()
#     lft = models.IntegerField()
#     rgt = models.IntegerField()
#     modified_on = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts_category_created_by')
#     modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts_category_modified_by')

#     def __str__(self):
#         return self.Accounts

#     class Meta:
#         verbose_name_plural = "Accounts"


# Create your models here.
# class Account(Organization):
#     class Meta:
#         proxy = True

#     class GroupsManagerMeta:
#         member_model = 'organization.OrganizationMember'

class AccountUser(models.Model):
    user_type = models.CharField(max_length=20, default='user')
    monthly_subscription = models.BooleanField(default=False)
    
    

# Dependency
# Company-FK  
# currency-FK