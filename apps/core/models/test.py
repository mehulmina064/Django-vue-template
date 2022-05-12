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
frequency_choices={('All','All'),('Hourly','Hourly'),('Hourly Long','Hourly Long'),('Daily','Daily'),('Daily Long','Daily Long'),('Weekly','Weekly'),('Weekly Long','Weekly Long'),('Monthly','Monthly'),('Monthly Long','Monthly Long'),('Cron','Cron'),('Yearly','Yearly'),('Annual','Annual')}

#script_types distionary with these fields
#DocType Event,Scheduler Event,Permission Query,API
script_types={('DocType Event','DocType Event'),('Scheduler Event','Scheduler Event'),('Permission Query','Permission Query'),('API','API')}

#doctype_events distionary with these fields
#Before Insert,Before Validate,Before Save,After Insert,After Save,Before Submit,After Submit,Before Cancel,After Cancel,Before Delete,After Delete,Before Save,After Save,On Payment Authorization
doctype_events={('Before Insert','Before Insert'),('Before Validate','Before Validate'),('Before Save','After Save'),('After Insert','After Insert'),('After Save','After Save'),('Before Submit','Before Submit'),('After Submit','After Submit'),('Before Cancel','Before Cancel'),('After Cancel','After Cancel'),('Before Delete','Before Delete'),('After Delete','After Delete'),('Before Save','Before Save'),('After Save','After Save'),('On Payment Authorization','On Payment Authorization')}

"""
create test table with fields as below:
test charfield


"""
class Test(models.Model):
    test = models.CharField(max_length=100)
    test2 = models.CharField(max_length=100)
    def __str__(self):
        return self.test
        
