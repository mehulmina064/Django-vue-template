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
create doctype_link table with fields as below:
link_doctype forigenkey to doctype
link_fieldname charfield
group charfield
hidden booleanfield
custom booleanfield
parent_doctype forigenkey to doctype related name- "is_child_table"
is_child_table booleanfield
table_fieldname charfield 

"""
class Doctype_Link(models.Model):
    link_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, related_name='link_doctype')
    link_fieldname = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    hidden = models.BooleanField(default=False)
    custom = models.BooleanField(default=False)
    parent_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, related_name='parent_doctype')
    is_child_table = models.BooleanField(default=False)
    table_fieldname = models.CharField(max_length=100)
    def __str__(self):
        return self.link_fieldname
    class Meta:
        verbose_name_plural = "doctype_links"
        ordering = ['link_fieldname']

    
