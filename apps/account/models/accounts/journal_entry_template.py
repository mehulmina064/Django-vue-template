from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from .company import Company


class JournalEntryTemplate(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)
    template_title = models.CharField(max_length=150, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='journal_entry_template_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='journal_entry_template_modified_by')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Journal_Entry_Template"
