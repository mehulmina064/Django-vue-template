from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from .data_import import Data_Import
# from .doctype import Doctype
# from .doctype_link import Doctype_Link
from .domain import Domain

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


item_types={('Route','Route'),('Action','Action'),('Separator','Separator')}


licence_types={('MIT License','MIT License'),('GNU General Public License','GNU General Public License'),('GNU Affero General','GNU Affero General'),('Public License','Public License')}


name_cases={('Title Case','Title Case'),('UPPER CASE','UPPER CASE')}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}
sort_orders={('ASC','ASC'),('DESC','DESC')}
document_types={('Document','Document'),('Setup','Setup'),('System','System'),('Other','Other')}
engine_={('InnoDB','InnoDB'),('MyISAM','MyISAM')}

#standard_types distionary with these fields
# Yes,No
standard_types={('Yes','Yes'),('No','No')} 

#report_types distionary with these fields
#Report Builder,Query Report,Script Report,Custom Report
report_types={('Report Builder','Report Builder'),('Query Report','Query Report'),('Script Report','Script Report'),('Custom Report','Custom Report')}


"""
create role table with fields as below:
role_name charfield
disabled booleannfield
desk_access booleanfield (default True)
two_factor_auth booleanfield (default False)
restrict_to_domain foreignkey(domain)
home_page charfield
search_bar booleanfield (default True)
list_sidebar booleanfield (default True)
bulk_actions booleanfield (default True)
form_sidebar   booleanfield (default True)
timeline booleanfield (default True)
dashboard booleanfield (default True)
view_switcher booleanfield (default True)
notifications  booleanfield (default True)
is_custom booleanfield (default False)


"""
class Role(models.Model):
    role_name = models.CharField(max_length=100,unique=True)
    disabled = models.BooleanField(default=False)
    desk_access = models.BooleanField(default=True)
    two_factor_auth = models.BooleanField(default=False)
    restrict_to_domain = models.ForeignKey(Domain,on_delete=CASCADE)
    home_page = models.CharField(max_length=100,default='home')
    search_bar = models.BooleanField(default=True)
    list_sidebar = models.BooleanField(default=True)
    bulk_actions = models.BooleanField(default=True)
    form_sidebar = models.BooleanField(default=True)
    timeline = models.BooleanField(default=True)
    dashboard = models.BooleanField(default=True)
    view_switcher = models.BooleanField(default=True)
    notifications = models.BooleanField(default=True)
    is_custom = models.BooleanField(default=False)
    def __str__(self):
        return self.role_name
    class Meta:
        verbose_name_plural = "Roles"
        ordering = ['role_name']

