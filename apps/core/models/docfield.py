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
F_Type={
('Autocomplete',''),('Attach',''),('Attach Image',''),('Barcode',''),('Button',''),('Check',''),('Code',''),('Color',''),('Column Break',''),('Currency',''),('Data',''),('Date',''),('Datetime',''),('Duration',''),('Dynamic Link',''),('Float',''),('Fold',''),('Geolocation',''),('Heading',''),('HTML',''),('HTML Editor',''),('Icon',''),('Image',''),('Int',''),('JSON',''),('Link',''),('Long Text',''),('Markdown Editor',''),('Password',''),('Percent',''),('Phone',''),('Read Only',''),('Rating',''),('Section Break',''),('Select',''),('Signature',''),('Small Text',''),('Tab Break',''),('Table',''),('Table MultiSelect',''),('Text',''),('Text Editor',''),('Time','')
}
Precision_No={
    ('1',''),('2',''),('3',''),('4',''),('5',''),('6',''),('7',''),('8',''),('9','')
}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}


"""
create docfield table with fields as below:
label charfield
fieldtype charfield  choices F_Type
fieldname charfield
reqd booleanField  default False
precision with choices precision_no
search_index booleanfield default false
in_list_view booleanfield defauld false
in_standard_filter booleanfield default false
in_global_search  booleanfield default false
in_preview booleanfield default false
allow_in_quick_entry booleanfield default false
bold booleanfield default false
translatable booleanfield default false
collapsbile booleanfield default false
collapsible_depends_on charfiled
options charfiled
default charfiled
fetch_from charfiled
fetch_if_empty booleanfield default false
depends_on charfiled
hidden booleanfield
print_width charfield
width charfield
description charfield
oldfieldname charfield
oldfieldtype charfield
mandatory_depends_on charfield
read_only_depends_on charfield

"""
class Docfield(models.Model):
    label=models.CharField(max_length=150,blank=True,null=True)
    fieldtype=models.CharField(max_length=150,choices=F_Type,blank=True,null=True)
    fieldname=models.CharField(max_length=150,blank=True,null=True)
    reqd=models.BooleanField(default=False)
    precision=models.CharField(max_length=150,choices=Precision_No,blank=True,null=True)
    search_index=models.BooleanField(default=False)
    in_list_view=models.BooleanField(default=False)
    in_standard_filter=models.BooleanField(default=False)
    in_global_search=models.BooleanField(default=False)
    in_preview=models.BooleanField(default=False)
    allow_in_quick_entry=models.BooleanField(default=False)
    bold=models.BooleanField(default=False)
    translatable=models.BooleanField(default=False)
    collapsible=models.BooleanField(default=False)
    collapsible_depends_on=models.CharField(max_length=150,blank=True,null=True)
    options=models.CharField(max_length=150,blank=True,null=True)
    default=models.CharField(max_length=150,blank=True,null=True)
    fetch_from=models.CharField(max_length=150,blank=True,null=True)
    fetch_if_empty=models.BooleanField(default=False)
    depends_on=models.CharField(max_length=150,blank=True,null=True)
    hidden=models.BooleanField(default=False)
    print_width=models.CharField(max_length=150,blank=True,null=True)
    width=models.CharField(max_length=150,blank=True,null=True)
    description=models.CharField(max_length=150,blank=True,null=True)
    oldfieldname=models.CharField(max_length=150,blank=True,null=True)
    oldfieldtype=models.CharField(max_length=150,blank=True,null=True)
    mandatory_depends_on=models.CharField(max_length=150,blank=True,null=True)
    read_only_depends_on=models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.label
    
    class Meta:
        db_table='docfield'
        verbose_name_plural='docfield'