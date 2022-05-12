from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# from .data_import import Data_Import
from .doctype import Doctype
# from .doctype_link import Doctype_Link
from .domain import Domain

from .role_profile import Role_Profile
from .role import Role
from .user_select_document_type import UserSelect_Document_Type
from .user_type_module import UserType_Module
from .language import Language
from .user_type import UserType
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
create user table with fields as below:
enabled boolean
email charfield
first_name charfield
middle_name charfield
last_name charfield
full_name charfield
send_welcome_email booleanfield
unsubscribed booleanfield
username charfield
language foreignkey to language table
time_zone charfield
Userimage imagefield
role_profile_name foreignkey to role_profile table
roles_html charfield
gender charfield
phone charfield
mobile_no charfield
birth_date datetimefield
location charfield
banner_image imagefield
interest charfield
bio charfield
mute_sounds boolean field
new_password passwordfield
logout_all_sessions booleanfield default true
reset_password_key charfield
last_password_reset_date datetimefield
redirect_url charfield
document_follow_notify booleanfield
document_follow_frequency charfield with choices defined in frequency_choices
thread_notify booleanfield default true
send_me_a_copy booleantype default false
allowed_in_mentions booleanfield default true
email_signature charfield
modules_html charfield
home_settings charfield
simultaneous_sessions initgerfield
Usertype foreign key to Usertype table
login_after intigerfield
login_before intigerfield
restrict_ip charfield
bypass_restrict_ip_check_if_2fa_enabled boolen field
last_login charfield default read only
last_ip charfield 
last_active datetime field
last_known_versions charfield
api_key charfield
api_secret passwordfield charfield
desk_theme charfield with choices theme_choices
module_profile foreign key to module
follow_created_documents booleanfield
follow_commented_documents booleanfield
follow_liked_documents booleanfield
follow_shared_documents booleanfield
follow_assigned_documents booleanfield

"""
class User(models.Model):
    enabled = models.BooleanField(default=True)
    email = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    send_welcome_email = models.BooleanField(default=False)
    unsubscribed = models.BooleanField(default=False)
    username = models.CharField(max_length=100,unique=True)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    time_zone = models.CharField(max_length=100)
    Userimage = models.ImageField(upload_to='Userimages',blank=True)
    role_profile_name = models.ForeignKey(Role_Profile,on_delete=models.CASCADE)
    roles_html = models.CharField(max_length=100)
    gender = models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    birth_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    banner_image = models.ImageField(upload_to='Userimages', blank=True, null=True)
    interest = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=100, blank=True, null=True)
    mute_sounds = models.BooleanField(default=False)
    new_password = models.CharField(max_length=100, blank=True, null=True)
    logout_all_sessions = models.BooleanField(default=True)
    reset_password_key = models.CharField(max_length=100, blank=True, null=True)
    last_password_reset_date = models.DateTimeField(blank=True, null=True)
    redirect_url = models.CharField(max_length=100, blank=True, null=True)
    document_follow_notify = models.BooleanField(default=True)
    document_follow_frequency = models.CharField(max_length=100, choices=frequency_choices, blank=True, null=True)
    thread_notify = models.BooleanField(default=True)
    send_me_a_copy = models.BooleanField(default=False)
    allowed_in_mentions = models.BooleanField(default=True)
    email_signature = models.CharField(max_length=100, blank=True, null=True)
    modules_html = models.CharField(max_length=100, blank=True, null=True)
    home_settings = models.CharField(max_length=100, blank=True, null=True)
    simultaneous_sessions = models.IntegerField(blank=True, null=True)
    Usertype = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, null=True)
    login_after = models.IntegerField(blank=True, null=True)
    login_before = models.IntegerField(blank=True, null=True)
    restrict_ip = models.CharField(max_length=100, blank=True, null=True)
    bypass_restrict_ip_check_if_2fa_enabled = models.BooleanField(default=False)
    last_login = models.CharField(max_length=100, blank=True, null=True)
    last_ip = models.CharField(max_length=100, blank=True, null=True)
    last_active = models.DateTimeField(blank=True, null=True)
    last_known_versions = models.CharField(max_length=100, blank=True, null=True)
    api_key = models.CharField(max_length=100, blank=True, null=True)
    api_secret = models.CharField(max_length=100, blank=True, null=True)
    desk_theme = models.CharField(max_length=100, choices=theme_choices, blank=True, null=True)
    # module_profile = models.ForeignKey(module, on_delete=models.CASCADE, blank=True, null=True)
    follow_created_documents = models.BooleanField(default=True)
    follow_commented_documents = models.BooleanField(default=True)
    follow_liked_documents = models.BooleanField(default=True)
    follow_shared_documents = models.BooleanField(default=True)
    follow_assigned_documents = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Users"





#language-fk
#module-fk
#Usertype-fk






