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
F_Type={
('Autocomplete',''),('Attach',''),('Attach Image',''),('Barcode',''),('Button',''),('Check',''),('Code',''),('Color',''),('Column Break',''),('Currency',''),('Data',''),('Date',''),('Datetime',''),('Duration',''),('Dynamic Link',''),('Float',''),('Fold',''),('Geolocation',''),('Heading',''),('HTML',''),('HTML Editor',''),('Icon',''),('Image',''),('Int',''),('JSON',''),('Link',''),('Long Text',''),('Markdown Editor',''),('Password',''),('Percent',''),('Phone',''),('Read Only',''),('Rating',''),('Section Break',''),('Select',''),('Signature',''),('Small Text',''),('Tab Break',''),('Table',''),('Table MultiSelect',''),('Text',''),('Text Editor',''),('Time','')
}
Precision_No={
    ('1',''),('2',''),('3',''),('4',''),('5',''),('6',''),('7',''),('8',''),('9','')
}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}


"""
create docshare table with fields as below:
user
share_doctype forigenkey to DocumentType
share_name forigenkey to DocumentType
read booleanfield default false
write booleanfield default false
share booleanfield default false
everyone booleanfield default false\
notify_by_email booleanfield default false
submit booleanfield default false

"""
class Docshare(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    share_doctype=models.ForeignKey(Doctype,on_delete=CASCADE)
    share_name=models.CharField(max_length=150,blank=True,null=True)
    read=models.BooleanField(default=False)
    write=models.BooleanField(default=False)
    share=models.BooleanField(default=False)
    everyone=models.BooleanField(default=False)
    notify_by_email=models.BooleanField(default=False)
    submit=models.BooleanField(default=False)

    def __str_submit_(self):
        return self.share_name
    class Meta:
        verbose_name_plural = "Shared Documents"
        db_table = 'docshare'

