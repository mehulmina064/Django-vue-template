from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
from .doctype import Doctype
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


"""
create report table with fields as below:
report_name char(100)
ref_doctype forigen key to doctype
reference_report charfield
is_standard with choices standard_types
module forigen key to modules
add_total_row boolean
report_type with choices report_types
disabled boolean
query charfield
javascript charfield
json charfield
roles forigen key to roles
disable_prepared_report boolean
prepared_report boolean
report_script charfield

"""
class Report(models.Model):
    report_name=models.CharField(max_length=100)
    ref_doctype=models.ForeignKey(Doctype,on_delete=CASCADE)
    reference_report=models.CharField(max_length=100,blank=True)
    is_standard=models.CharField(max_length=100,choices=standard_types)
    # module=models.ForeignKey(modules,on_delete=CASCADE)
    add_total_row=models.BooleanField(default=False)
    report_type=models.CharField(max_length=100,choices=report_types)
    disabled=models.BooleanField(default=False)
    query=models.CharField(max_length=100,blank=True)
    javascript=models.CharField(max_length=100,blank=True)
    json=models.CharField(max_length=100,blank=True)
    roles=models.ForeignKey(Role,on_delete=CASCADE)
    disable_prepared_report=models.BooleanField(default=False)
    prepared_report=models.BooleanField(default=False)
    report_script=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.report_name





#modules-fk