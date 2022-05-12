from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from apps.core.models.doctype import Doctype

#create Activity_Log table with fields as below:
#subject
#content
#now
#operation select type from ("\nlogin", "\nlogout")
#status
#reference_doctype
#reference_name_owner
#timeline_doctype
#timeline_name
#link_doctype forigen key to doctype
#ink_name
#user
#full_name
class Activity_Log(models.Model):
    subject = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=150, blank=True, null=True)
    now = models.DateTimeField(auto_now=True)
    operation = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=150, blank=True, null=True)
    reference_doctype = models.CharField(max_length=150, blank=True, null=True)
    reference_name_owner = models.CharField(max_length=150, blank=True, null=True)
    timeline_doctype = models.CharField(max_length=150, blank=True, null=True)
    timeline_name = models.CharField(max_length=150, blank=True, null=True)
    link_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, blank=True, null=True)
    link_name = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name_plural = "Activity_Log"

#doctype-fk