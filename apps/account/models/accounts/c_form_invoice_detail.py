from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# from .sales_invoice import SalesInvoice
# from .territory_item import Territory


class CFormInvoiceDetail(models.Model):
    # invoice_no = models.ForeignKey(SalesInvoice, on_delete=CASCADE, blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=True)
    # territory = models.ForeignKey(Territory, on_delete=CASCADE, blank=True, null=True)
    net_total = models.DecimalField(max_digits=25, decimal_places=3)
    grand_total = models.DecimalField(max_digits=25, decimal_places=2)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='c_form_invoice_detail_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='c_form_invoice_detail_modified_by')

    def __str__(self):
        return self.invoice_no

    class Meta:
        verbose_name_plural = "C_Form_Invoice_Detail"

#sales_invoice-FK
#territory-FK