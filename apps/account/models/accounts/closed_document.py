from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .bank_account import DocType


class ClosedDocument(models.Model):
    document_type = models.ForeignKey(DocType, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='closed_document._created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='closed_document_modified_by')

    def __str__(self):
        return self.document_type

    class Meta:
        verbose_name_plural = "Closed_Document"
