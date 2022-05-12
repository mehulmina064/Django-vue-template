from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from apps.core.models.doctype import Doctype

#create comment table with fields as below:
#comment
#comment_email
#subject
#comment_by
#reference_doctype 
#link_doctype  forigen key to doctype
#link_name
#reference_owner
#content
class Comment(models.Model):
    comment = models.CharField(max_length=150, blank=True, null=True)
    comment_email = models.CharField(max_length=150, blank=True, null=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    comment_by = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    reference_doctype = models.CharField(max_length=150, blank=True, null=True)
    link_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, blank=True, null=True)
    link_name = models.CharField(max_length=150, blank=True, null=True)
    reference_owner = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.comment
    class Meta:
        verbose_name_plural = "Comment"
#doctype-fk
