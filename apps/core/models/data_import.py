import csv
from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from .role import Role

# from apps.core.models.doctype import Doctype

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}

"""
create data_import table with fields as below:
reference_doctype forigen key to DocumentType
file_type with choices as csv, excel
import_type with choices as {('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
import_file
template_options jasonfield
Pending with choices  
template_warnings
submit_after_import boolean field default false
mute_emails boolean field default true
show_failed_logs boolean field default false
google_sheets_url URLField
refresh_google_sheet charfield
payload_count intiger field

"""

class Data_Import(models.Model):
    # reference_doctype= models.ForeignKey(Doctype,on_delete=CASCADE,blank=True,null=True)
    file_type = models.CharField(max_length=150, blank=True, null=True,choices=Field_Types,default='csv')
    import_type = models.CharField(max_length=150, blank=True, null=True,choices=import_types,default='Insert New Records')
    import_file=models.CharField(max_length=150,blank=True,null=True)
    template_options=models.TextField(blank=True,null=True)
    Pending=models.CharField(max_length=150,blank=True,null=True,choices=pending_types,default='Success')
    template_warnings=models.TextField(blank=True,null=True)
    submit_after_import=models.BooleanField(default=False)
    mute_emails=models.BooleanField(default=True)
    show_failed_logs=models.BooleanField(default=False)
    google_sheets_url=models.URLField(blank=True,null=True)
    refresh_google_sheet=models.CharField(max_length=150,blank=True,null=True)
    payload_count=models.IntegerField(default=0)

    def __str__(self):
        return self.import_file
    
    class Meta:
        db_table = 'data_import'


    