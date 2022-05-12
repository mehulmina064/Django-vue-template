from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

#create block_module table with fields as below:
#module
class Block_Module(models.Model):
    module = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.module
    class Meta:
        verbose_name_plural = "Block_Module"

