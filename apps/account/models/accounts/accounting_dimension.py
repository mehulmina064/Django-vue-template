from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Accounting_Dimension(models.Model):
    fieldname = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='accounting_dimension_category_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='accounting_dimension_category_modified_by')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = "Accounting_Dimension"

