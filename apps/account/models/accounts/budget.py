from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# from . import monthlydistribution
from .company import Company
from .cost_center import CostCenter
# from .fiscalyear import FiscalYear
# from .psoaproject import Project


class Budget(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    cost_center = models.ForeignKey(CostCenter, on_delete=CASCADE, blank=True, null=True)
    # project = models.ForeignKey(Project, on_delete=CASCADE, blank=True, null=True)
    # fiscal_year = models.ForeignKey(FiscalYear, on_delete=CASCADE, blank=True, null=True)
    # monthly_distribution = models.ForeignKey(monthlydistribution, on_delete=CASCADE, blank=True, null=True)
    # amended_from = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='budget_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='budget_modified_by')

    def __str__(self):
        return self.company



# company-FK
#cost_center-FK
#project-FK
#fiscal_year-FK
#monthly_distribution-FK