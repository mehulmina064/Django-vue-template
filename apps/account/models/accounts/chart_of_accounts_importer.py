from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company


class ChartOfAccountsImporter(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    import_file = models.FileField(upload_to=None, max_length=254)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='chart_of_accounts_importer_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='chart_of_accounts_importer_modified_by')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Chart_Of_Accounts_Importer"

#company-FK