from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class FinanceBook(models.Model):
    finance_book_name = models.CharField(max_length=200, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='finance_book_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='finance_book_modified_by')

    def __str__(self):
        return self.finance_book_name

    class Meta:
        verbose_name_plural = "Finance_Book"
