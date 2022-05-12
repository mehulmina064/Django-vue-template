from django.db import models


class Currency(models.Model):
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Currency"
