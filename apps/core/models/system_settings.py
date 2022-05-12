from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
# from .doctype import Doctype
# from .doctype_link import Doctype_Link
# from .domain import Domain

from .language import Language

Field_Types = (
    ('csv','CSV'),
    ('excel', 'EXCEL'),
)
F_Type={
('Autocomplete',''),('Attach',''),('Attach Image',''),('Barcode',''),('Button',''),('Check',''),('Code',''),('Color',''),('Column Break',''),('Currency',''),('Data',''),('Date',''),('Datetime',''),('Duration',''),('Dynamic Link',''),('Float',''),('Fold',''),('Geolocation',''),('Heading',''),('HTML',''),('HTML Editor',''),('Icon',''),('Image',''),('Int',''),('JSON',''),('Link',''),('Long Text',''),('Markdown Editor',''),('Password',''),('Percent',''),('Phone',''),('Read Only',''),('Rating',''),('Section Break',''),('Select',''),('Signature',''),('Small Text',''),('Tab Break',''),('Table',''),('Table MultiSelect',''),('Text',''),('Text Editor',''),('Time','')
}
float_precision_no={
    ('2',''),('3',''),('4',''),('5',''),('6',''),('7',''),('8',''),('9','')
}

Precision_No={
    ('0',''),('1',''),('2',''),('3',''),('4',''),('5',''),('6',''),('7',''),('8',''),('9','')
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
frequency_choices={('All','All'),('Hourly','Hourly'),('Hourly Long','Hourly Long'),('Daily','Daily'),('Daily Long','Daily Long'),('Weekly','Weekly'),('Weekly Long','Weekly Long'),('Monthly','Monthly'),('Monthly Long','Monthly Long'),('Cron','Cron'),('Yearly','Yearly'),('Annual','Annual')}

#script_types distionary with these fields
#DocType Event,Scheduler Event,Permission Query,API
script_types={('DocType Event','DocType Event'),('Scheduler Event','Scheduler Event'),('Permission Query','Permission Query'),('API','API')}

#doctype_events distionary with these fields
#Before Insert,Before Validate,Before Save,After Insert,After Save,Before Submit,After Submit,Before Cancel,After Cancel,Before Delete,After Delete,Before Save,After Save,On Payment Authorization
doctype_events={('Before Insert','Before Insert'),('Before Validate','Before Validate'),('Before Save','After Save'),('After Insert','After Insert'),('After Save','After Save'),('Before Submit','Before Submit'),('After Submit','After Submit'),('Before Cancel','Before Cancel'),('After Cancel','After Cancel'),('Before Delete','Before Delete'),('After Delete','After Delete'),('Before Save','Before Save'),('After Save','After Save'),('On Payment Authorization','On Payment Authorization')}

#date_formats distionary with these fields
#yyyy-mm-dd,ndd-mm-yyyy,ndd/mm/yyyy,ndd.mm.yyyy,nmm/dd/yyyy,nmm-dd-yyyy
date_formats={('ymd','yyyy-mm-dd'),('dmy','dd-mm-yyyy'),('dmy','dd/mm/yyyy'),('dmy','dd.mm.yyyy'),('mdy','mm/dd/yyyy'),('mdy','mm-dd-yyyy')}

#time_formats distionary with these fields
#HH:mm:ss,HH:mm
time_formats={('24','HH:mm:ss'),('12','HH:mm')}

#week_ starts on distionary with these fields
#Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday
week_={('Sunday','Sunday'),('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday')}

"""
create system_settings table with fields as below:
country forign key to country table
language forign key to language table
time_zone charfield
setup_complete booleanfield
date_format charfield with choices date_formats
time_format charfield with choices time_formats
number_format charfield
float_precision charfield with choices float_precision_no
currency_precision charfield with choices precision_no
backup_limit integerfield default 3
enable_scheduler booleanfield
apply_strict_User_permissions booleanfield
session_expiry charfield
session_expiry_mobile charfield
deny_multiple_sessions booleanfield
allow_login_using_mobile_number booleanfield
allow_login_using_User_name booleanfield
allow_error_traceback booleanfield default 1
force_User_to_reset_password integerfield
enable_password_policy booleanfield
minimum_password_score charfield
allow_consecutive_login_attempts integerfield
allow_login_after_fail integerfield
enable_two_factor_auth booleanfield
bypass_2fa_for_retricted_ip_users booleanfield
bypass_restrict_ip_check_if_2fa_enabled booleanfield
two_factor_method charfield with choices ['OTP App','SMS','Email']
lifespan_qrcode_image integerfield
otp_issuer_name charfield
email_footer_address charfield
disable_standard_email_footer booleanfield
hide_footer_in_auto_email_reports booleanfield
allow_guests_to_upload_files booleanfield
dormant_days integerfield
password_reset_limit integerfield
logout_on_password_reset booleanfield default 1
enable_onboarding booleanfield
attach_view_link booleanfield default 1
prepared_report_expiry_period integerfield default 30
enable_prepared_report_auto_deletion booleanfield default 1
app_name charfield
strip_exif_metadata_from_uploaded_images booleanfield default 1
encrypt_backup booleanfield 
disable_system_update_notification booleanfield 
first_day_of_the_week charfield with choices week_ default 'Sunday'
max_auto_email_report_per_user integerfield default 20

"""
class System_Settings(models.Model):
    # country=models.ForeignKey(country,on_delete=models.CASCADE)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)
    time_zone=models.CharField(max_length=100)
    setup_complete=models.BooleanField(default=False)
    date_format=models.CharField(max_length=100,choices=date_formats)
    time_format=models.CharField(max_length=100,choices=time_formats)
    number_format=models.CharField(max_length=100)
    float_precision=models.CharField(max_length=100,choices=float_precision_no)
    currency_precision=models.CharField(max_length=100,choices=Precision_No)
    backup_limit=models.IntegerField(default=3)
    enable_scheduler=models.BooleanField(default=False)
    apply_strict_User_permissions=models.BooleanField(default=False)
    session_expiry=models.CharField(max_length=100)
    session_expiry_mobile=models.CharField(max_length=100)
    deny_multiple_sessions=models.BooleanField(default=False)
    allow_login_using_mobile_number=models.BooleanField(default=False)
    allow_login_using_User_name=models.BooleanField(default=False)
    allow_error_traceback=models.BooleanField(default=True)
    force_User_to_reset_password=models.IntegerField(default=0)
    enable_password_policy=models.BooleanField(default=False)
    minimum_password_score=models.CharField(max_length=100)
    allow_consecutive_login_attempts=models.IntegerField(default=0)
    allow_login_after_fail=models.IntegerField(default=0)
    enable_two_factor_auth=models.BooleanField(default=False)
    bypass_2fa_for_retricted_ip_users=models.BooleanField(default=False)
    bypass_restrict_ip_check_if_2fa_enabled=models.BooleanField(default=False)
    two_factor_method=models.CharField(max_length=100)
    lifespan_qrcode_image=models.IntegerField(default=0)
    otp_issuer_name=models.CharField(max_length=100)
    email_footer_address=models.CharField(max_length=100)
    disable_standard_email_footer=models.BooleanField(default=False)
    hide_footer_in_auto_email_reports=models.BooleanField(default=False)
    allow_guests_to_upload_files=models.BooleanField(default=False)
    dormant_days=models.IntegerField(default=0)
    password_reset_limit=models.IntegerField(default=0)
    logout_on_password_reset=models.BooleanField(default=True)
    enable_onboarding=models.BooleanField(default=False)
    attach_view_link=models.BooleanField(default=True)
    prepared_report_expiry_period=models.IntegerField(default=30)
    enable_prepared_report_auto_deletion=models.BooleanField(default=False)
    app_name=models.CharField(max_length=100)
    strip_exif_metadata_from_uploaded_images=models.BooleanField(default=True)
    encrypt_backup=models.BooleanField(default=False)
    disable_system_update_notification=models.BooleanField(default=False)
    first_day_of_the_week=models.CharField(max_length=100,choices=week_,default='Sunday')
    max_auto_email_report_per_user=models.IntegerField(default=20)
    def __str__(self):
        return self.app_name


    


#language-fk
#country-fk