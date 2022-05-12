from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role

from apps.core.models.doctype import Doctype

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)



#create data_export table with fields as below:
#reference_doctype forigen key to DocumentType
#file_type with choices as csv, excel
class Data_Export(models.Model):
    reference_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, blank=True, null=True)
    file_type = models.CharField(max_length=150, blank=True, null=True,choices=Field_Types,default='csv')
    def __str__(self):
        return self.file_type
    class Meta:
        verbose_name_plural = "Data_Export"
