from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .bank_account import DocType


class BankClearanceDetail(models.Model):
    payment_document = models.ForeignKey(DocType, on_delete=CASCADE)
    against_account = models.CharField(max_length=200)
    amount = models.CharField(max_length=150)
    posting_date = models.DateField()
    cheque_number = models.PositiveIntegerField(validators=[MaxValueValidator(6)], unique=True)
    cheque_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    clearance_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bank_clearance_detail_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='bank_clearance_detail_modified_by')

    def __str__(self):
        return self.payment_document

    class Meta:
        verbose_name_plural = "Bank_Clearance_Detail"
