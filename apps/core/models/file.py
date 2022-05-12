from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
from .doctype import Doctype
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
create file table with fields as below:
file_name charfielld
preview charfielld
preview_html charfielld
is_home_folder booleanfield
is_attachments_folder booleanfield
file_size intfield
file_url charfielld
thumbnail_url charfielld maxlength=100
folder foreignkey to folder
is_folder booleanfield
attached_to_doctype foreignkey to doctype
attached_to_name charfielld
attached_to_field charfielld
old_parent charfielld
content_hash charfielld
uploaded_to_dropbox booleanfield
uploaded_to_google_drive booleanfield


"""
class File(models.Model):
    file_name = models.CharField(max_length=100)
    preview = models.CharField(max_length=100)
    preview_html = models.CharField(max_length=100)
    is_home_folder = models.BooleanField(default=False)
    is_attachments_folder = models.BooleanField(default=False)
    file_size = models.IntegerField(default=0)
    file_url = models.CharField(max_length=100)
    thumbnail_url = models.CharField(max_length=100)
    # folder = models.ForeignKey('folder', on_delete=CASCADE)
    is_folder = models.BooleanField(default=False)
    attached_to_doctype = models.ForeignKey(Doctype, on_delete=CASCADE)
    attached_to_name = models.CharField(max_length=100)
    attached_to_field = models.CharField(max_length=100)
    old_parent = models.CharField(max_length=100)
    content_hash = models.CharField(max_length=100)
    uploaded_to_dropbox = models.BooleanField(default=False)
    uploaded_to_google_drive = models.BooleanField(default=False)
    def __str__(self):
        return self.file_name
    
    #folder-fk



        




