from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .dunning import Language


class DunningLetterText(models.Model):
    language = models.ForeignKey(Language, on_delete=CASCADE, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='dunning_letter_text_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='dunning_letter_text_modified_by')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = "Dunning_Letter_Text"
