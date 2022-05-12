from pyexpat import model
from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from apps.core.models.doctype import Doctype

#create communication_link table with fields as below:
#link_doctype forigen key to DocumentType
#link_name  
#link_title
class Communication_Link(models.Model):
    link_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, blank=True, null=True)
    link_name = models.CharField(max_length=150, blank=True, null=True)
    link_title = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.link_title
    class Meta:
        verbose_name_plural = "Communication_Link"