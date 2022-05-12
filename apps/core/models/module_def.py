from .package import Package
from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role
# from .data_import import Data_Import
# from .doctype import Doctype
# from .doctype_link import Doctype_Link
from .package import Package
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
name_cases={('Title Case','Title Case'),('UPPER CASE','UPPER CASE')}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}
sort_orders={('ASC','ASC'),('DESC','DESC')}
document_types={('Document','Document'),('Setup','Setup'),('System','System'),('Other','Other')}
engine_={('InnoDB','InnoDB'),('MyISAM','MyISAM')}
"""
create module_def table with fields as below:
module_name charfiild(max_length=100)
app_name charfield(max_length=100)
restrict_to_domain forigen key to domain
custom charfield(max_length=100)
package forigen key to package


"""
class Module_Def(models.Model):
    module_name = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    restrict_to_domain = models.ForeignKey(Domain, on_delete=CASCADE)
    custom = models.CharField(max_length=100)
    package = models.ForeignKey(Package, on_delete=CASCADE)
    def __str__(self):
        return self.module_name
    class Meta:
        verbose_name_plural = "Module Def"
        db_table = 'module_def'

#package -FK




