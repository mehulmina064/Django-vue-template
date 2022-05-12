from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}

"""
create defaultvalue table with fields as below:
defkey charfield
"""

class DefaultValue(models.Model):
    defkey=models.CharField(max_length=150,blank=True,null=True)
    defvalue=models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return self.defkey

    class Meta:
        verbose_name_plural = "Default Values"
        db_table = 'defaultvalue'
