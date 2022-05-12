from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
# from .doctype import Doctype
# from .doctype_link import Doctype_Link
Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
F_Type={
('Autocomplete',''),('Attach',''),('Attach Image',''),('Barcode',''),('Button',''),('Check',''),('Code',''),('Color',''),('Column Break',''),('Currency',''),('Data',''),('Date',''),('Datetime',''),('Duration',''),('Dynamic Link',''),('Float',''),('Fold',''),('Geolocation',''),('Heading',''),('HTML',''),('HTML Editor',''),('Icon',''),('Image',''),('Int',''),('JSON',''),('Link',''),('Long Text',''),('Markdown Editor',''),('Password',''),('Percent',''),('Phone',''),('Read Only',''),('Rating',''),('Section Break',''),('Select',''),('Signature',''),('Small Text',''),('Tab Break',''),('Table',''),('Table MultiSelect',''),('Text',''),('Text Editor',''),('Time','')
}
Precision_No={
    ('1',''),('2',''),('3',''),('4',''),('5',''),('6',''),('7',''),('8',''),('9','')
}
name_cases={('Title Case','Title Case'),('UPPER CASE','UPPER CASE')}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}
sort_orders={('ASC','ASC'),('DESC','DESC')}
document_types={('Document','Document'),('Setup','Setup'),('System','System'),('Other','Other')}
engine_={('InnoDB','InnoDB'),('MyISAM','MyISAM')}
"""
create error_snapshot table with fields as below:
view charfield with max length 400
seen boolean field
evalue charfield 
timestamp datefield
relapses intfield
etype charfield
traceback charfield
parent_error_snapshot charfield
pyver charfield
exception charfield
locals charfield
frames charfield


"""
class Error_Snapshot(models.Model):
    view = models.CharField(max_length=400)
    seen = models.BooleanField(default=False)
    evalue = models.CharField(max_length=100)
    timestamp = models.DateField()
    relapses = models.IntegerField()
    etype = models.CharField(max_length=100)
    traceback = models.CharField(max_length=100)
    parent_error_snapshot = models.ForeignKey("self", on_delete=CASCADE, null=True, blank=True)
    pyver = models.CharField(max_length=100)    
    exception = models.CharField(max_length=100)
    locals = models.CharField(max_length=100)
    frames = models.CharField(max_length=100)   
    def __str__(self):
        return self.view
    class Meta:
        verbose_name_plural = "Error Snapshots"
        ordering = ['-timestamp']
        

        




