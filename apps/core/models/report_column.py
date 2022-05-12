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

#fieldtypes dictionary with these fields
#boolean,Currency,charfield,Date,DateField,ForeignKey,Float,IntigerField
#ManyToManyField,ManyToOneRelation,OneToManyRelation,OneToOneRelation
fieldtypes={('boolean','boolean'),('Currency','Currency'),('charfield','charfield'),('Date','Date'),('DateField','DateField'),('ForeignKey','ForeignKey'),('Float','Float'),('IntigerField','IntigerField'),('ManyToManyField','ManyToManyField'),('ManyToOneRelation','ManyToOneRelation'),('OneToManyRelation','OneToManyRelation'),('OneToOneRelation','OneToOneRelation')}


#report_types distionary with these fields
#Report Builder,Query Report,Script Report,Custom Report
report_types={('Report Builder','Report Builder'),('Query Report','Query Report'),('Script Report','Script Report'),('Custom Report','Custom Report')}


"""
create report_column table with fields as below:
fieldname charfield(255)
label charfield(255)
fieldtype with choices fieldtypes
options charfield(255)
width intigerfield

"""
class Report_Column(models.Model):
    fieldname = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    fieldtype = models.CharField(max_length=255,choices=fieldtypes)
    options = models.CharField(max_length=255)
    width = models.IntegerField()
    def __str__(self):
        return self.fieldname
    class Meta:
        db_table = 'report_column'
        verbose_name_plural = 'Report Columns'
        verbose_name = 'Report Column'
        ordering = ['id']
