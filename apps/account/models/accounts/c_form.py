from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .company import Company
# from ..selling.customer import Customer


class CForm(models.Model):
    c_form_no = models.CharField(max_length=200, blank=True, null=True)
    received_date = models.DateField()
    # customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True, null=True)
    company = models.ForeignKey(models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True))
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    state = models.CharField(max_length=200, blank=True, null=True)
    total_invoiced_amount = models.DecimalField(max_digits=20, decimal_places=2)
    # amended_from = models.ForeignKey(CForm, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='C_Form_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='C_Form_modified_by')

    def __str__(self):
        return self.c_form_no

    class Meta:
        verbose_name_plural = "C_Forms"

# company-FK
# customer-FK