from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
from apps.core.models.doctype import Doctype
# from .data_import import Data_Import

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}


"""
create deleted_document table with fields as below:
deleted_name charfield
deleted_doctype forigen key to DocumentType
restored boolean field default false
new_name charfield readonly
data charfield

"""
class Deleted_Document(models.Model):
    deleted_name=models.CharField(max_length=150,blank=True,null=True)
    deleted_doctype=models.ForeignKey(Doctype,on_delete=CASCADE,blank=True,null=True)
    restored=models.BooleanField(default=False)
    new_name=models.CharField(max_length=150,blank=True,null=True)
    data=models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return self.deleted_name
    class Meta:
        verbose_name_plural = "Deleted Documents"
        db_table = 'deleted_document'
        
