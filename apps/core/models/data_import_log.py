from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
from .data_import import Data_Import

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}

#create data_import_log table with fields as below:
#data_import forigen key to data_import
#docname charfield
#exception charfield
#success boolean field default false
#log_index intiger field
#messages charfield
class Data_Import_Log(models.Model):
    data_import=models.ForeignKey(Data_Import,on_delete=CASCADE,blank=True,null=True)
    docname=models.CharField(max_length=150,blank=True,null=True)
    doc_type=models.CharField(max_length=150,blank=True,null=True,choices=Field_Types)
    exception=models.CharField(max_length=150,blank=True,null=True)
    success=models.BooleanField(default=False)
    log_index=models.IntegerField(default=0)
    messages=models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self):
        return self.exception
    
    class Meta:
        db_table = 'data_import_log'
        

    