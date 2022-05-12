from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
from .doctype import Doctype
# from .doctype_link import Doctype_Link
from .domain import Domain

# from role_profile import role_profile
# from .role import Role
from .user_select_document_type import UserSelect_Document_Type
# from .Usertype_module import UserType_Module
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

#status_choices distionary with these fields
#Scheduled,Complete,Failed
status_choices={('Scheduled','Scheduled'),('Complete','Complete'),('Failed','Failed')}

#frequency_choices distionary with these fields
#All,Hourly,Hourly Long,Daily,Daily Long,Weekly,Weekly Long,Monthly,Monthly Long,Cron,Yearly,Annual
frequency_choices={('All','All'),('Hourly','Hourly'),('Daily','Daily'),('Weekly','Weekly')}

#script_types distionary with these fields
#DocType Event,Scheduler Event,Permission Query,API
script_types={('DocType Event','DocType Event'),('Scheduler Event','Scheduler Event'),('Permission Query','Permission Query'),('API','API')}

#doctype_events distionary with these fields
#Before Insert,Before Validate,Before Save,After Insert,After Save,Before Submit,After Submit,Before Cancel,After Cancel,Before Delete,After Delete,Before Save,After Save,On Payment Authorization
doctype_events={('Before Insert','Before Insert'),('Before Validate','Before Validate'),('Before Save','After Save'),('After Insert','After Insert'),('After Save','After Save'),('Before Submit','Before Submit'),('After Submit','After Submit'),('Before Cancel','Before Cancel'),('After Cancel','After Cancel'),('Before Delete','Before Delete'),('After Delete','After Delete'),('Before Save','Before Save'),('After Save','After Save'),('On Payment Authorization','On Payment Authorization')}

#theme_choices distionary with those fields
#Light,Dark,Automatic
theme_choices={('Light','Light'),('Dark','Dark'),('Automatic','Automatic')}

"""
create Usertype table with fields as below:
is_standard booleanfield
#Userdoctypes table type
role foreignkey to Role table
select_doctypes foreignkey to Userselect_document_type table
apply_Userpermission_on foreign key to doctype table
Userid_field charfield
modified_by charfield
modified_date datetimefield
created_by charfield
created_date datetimefield
Usertype_modules foreign key to Usertype_module table


"""
class UserType(models.Model):
    is_standard = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    select_doctypes = models.ForeignKey(UserSelect_Document_Type, on_delete=models.CASCADE)
    apply_Userpermission_on = models.ForeignKey(Doctype, on_delete=models.CASCADE)
    Userid_field = models.CharField(max_length=100, blank=True, null=True)
    modified_by = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    Usertype_modules = models.CharField(max_length=400,blank=True)
    name=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'Usertype'
        verbose_name_plural = 'User Type'
        verbose_name = 'User Type'
    
    def __str__(self):
        return self.role.name

