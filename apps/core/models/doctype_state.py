from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
from .doctype import Doctype

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
F_Type={
('Autocomplete',''),('Attach',''),('Attach Image',''),('Barcode',''),('Button',''),('Check',''),('Code',''),('Color',''),('Column Break',''),('Currency',''),('Data',''),('Date',''),('Datetime',''),('Duration',''),('Dynamic Link',''),('Float',''),('Fold',''),('Geolocation',''),('Heading',''),('HTML',''),('HTML Editor',''),('Icon',''),('Image',''),('Int',''),('JSON',''),('Link',''),('Long Text',''),('Markdown Editor',''),('Password',''),('Percent',''),('Phone',''),('Read Only',''),('Rating',''),('Section Break',''),('Select',''),('Signature',''),('Small Text',''),('Tab Break',''),('Table',''),('Table MultiSelect',''),('Text',''),('Text Editor',''),('Time','')
}
colors={
    ('1','Blue'),('2','Cyan'),('3','Gray'),('4','Green'),('5','Light Blue'),('6','Orange'),('7','Pink'),('8','Purple'),('9','Red'),('10','Yellow'),
}
name_cases={('Title Case','Title Case'),('UPPER CASE','UPPER CASE')}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}
sort_orders={('ASC','ASC'),('DESC','DESC')}
document_types={('Document','Document'),('Setup','Setup'),('System','System'),('Other','Other')}
engine_={('InnoDB','InnoDB'),('MyISAM','MyISAM')}
"""
create doctype_state table with fields as below:
title charfield
color with choices colors 
custom booleanfield

"""
class Doctype_State(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100,choices=colors)
    custom = models.BooleanField(default=False)
    doctype = models.ForeignKey(Doctype, on_delete=CASCADE)
    class Meta:
        verbose_name_plural = "Document Type States"

    def __str__(self):
        return self.title



    
