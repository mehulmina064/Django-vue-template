from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role

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
name_cases={('Title Case','Title Case'),('UPPER CASE','UPPER CASE')}
import_types={('Insert New Records','Insert New Records'),('Update Existing Records','Update Existing Records'),}
pending_types={('Success','Success'),('Partial Success','Partial Success'),('Error','Error')}
sort_orders={('ASC','ASC'),('DESC','DESC')}
document_types={('Document','Document'),('Setup','Setup'),('System','System'),('Other','Other')}
engine_={('InnoDB','InnoDB'),('MyISAM','MyISAM')}
"""
create doctype abstract table with fields as below:
module  connect to module 
is_submittable booleanfield default false
istable booleanfield default false
issingle booleanfield default false
editable_grid booleanfield default false
quick_entry booleanfield default false
track_changes booleanfield default false
track_seen booleanfield default false
track_views booleanfield default false
custom booleanfield default false
beta booleanfield 
fields charfield
autoname charfield
name_case with choices name_cases
description charfield
image_field imagefield
timeline_field charfield
max_attachments intigerfield
hide_toolbar booleanfield default false
allow_copy booleanfield false
allow_rename booleanfield false
allow_import booleanfield
allow_events_in_timeline booleanfield
allow_auto_repeat booleanfield
title_field charfield
search_fields fieldtype
default_print_format charfield
sort_field charfield
sort_order with choices sort_orders
document_type choices document_types
icon charfield
color charfiled
show_preview_popup booleanfield 
show_name_in_global_search booleanfield
#permissions table type
in_create boolean type
has_web_view booleantype
allow_guest_to_view booleantype
engine witch choices engine_
is_tree booleantype
nsm_parent_field charfield
documentation forigen key witch DocumentType
#actions table type
sender_field charfield
email_append_to booleanfield
index_web_pages_for_search booleanfield default True
is_virtual booleantype
default_email_template forigen key to email_template
website_search_field charfield
migration_hash charfield
show_title_field_in_link boolean field

"""
class Doctype(models.Model):
    module=models.CharField(max_length=150,blank=True,null=True)
    is_submittable=models.BooleanField(default=False)
    istable=models.BooleanField(default=False)
    issingle=models.BooleanField(default=False)
    editable_grid=models.BooleanField(default=False)
    quick_entry=models.BooleanField(default=False)
    track_changes=models.BooleanField(default=False)
    track_seen=models.BooleanField(default=False)
    track_views=models.BooleanField(default=False)
    custom=models.BooleanField(default=False)
    beta=models.BooleanField(default=False)
    fields=models.CharField(max_length=255,blank=True,null=True)
    autoname=models.CharField(max_length=255,blank=True,null=True)
    name_case=models.CharField(max_length=255,choices=name_cases,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    image_field=models.ImageField(upload_to='doctype_images',blank=True,null=True)
    timeline_field=models.CharField(max_length=255,blank=True,null=True)
    max_attachments=models.IntegerField(blank=True,null=True)
    hide_toolbar=models.BooleanField(default=False)
    allow_copy=models.BooleanField(default=False)
    allow_rename=models.BooleanField(default=False)
    allow_import=models.BooleanField(default=False)
    allow_events_in_timeline=models.BooleanField(default=False)
    allow_auto_repeat=models.BooleanField(default=False)
    title_field=models.CharField(max_length=255,blank=True,null=True)
    search_fields=models.CharField(max_length=255,blank=True,null=True)
    default_print_format=models.CharField(max_length=255,blank=True,null=True)
    sort_field=models.CharField(max_length=255,blank=True,null=True)
    sort_order=models.CharField(max_length=255,choices=sort_orders,blank=True,null=True)
    document_type=models.CharField(max_length=255,choices=document_types,blank=True,null=True)
    icon=models.CharField(max_length=255,blank=True,null=True)
    color=models.CharField(max_length=255,blank=True,null=True)
    show_preview_popup=models.BooleanField(default=False)
    show_name_in_global_search=models.BooleanField(default=False)
    #permissions table type
    in_create=models.BooleanField(default=False)
    has_web_view=models.BooleanField(default=False)
    allow_guest_to_view=models.BooleanField(default=False)
    engine=models.CharField(max_length=255,choices=engine_,blank=True,null=True)
    is_tree=models.BooleanField(default=False)
    nsm_parent_field=models.CharField(max_length=255,blank=True,null=True)
    documentation=models.ForeignKey("Doctype",on_delete=CASCADE,blank=True,null=True)
    #actions table type
    sender_field=models.CharField(max_length=255,blank=True,null=True)
    email_append_to=models.BooleanField(default=False)
    index_web_pages_for_search=models.BooleanField(default=False)
    is_virtual=models.BooleanField(default=False)
    # default_email_template=models.ForeignKey(EmailTemplate,on_delete=CASCADE,blank=True,null=True)
    website_search_field=models.CharField(max_length=255,blank=True,null=True)
    migration_hash=models.CharField(max_length=255,blank=True,null=True)
    show_title_field_in_link=models.BooleanField(default=False)
    
    class Meta:
        db_table='doctype'
        verbose_name_plural='doctypes'

    def __str__(self):
        return self.name

# EmailTemplate-fk

