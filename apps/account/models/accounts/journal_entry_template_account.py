from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .account import Account


class JournalEntryTemplateAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = "JournalEntryTemplateAccount"
