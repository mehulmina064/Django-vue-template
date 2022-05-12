from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

from apps.core.models.doctype import Doctype

#create communication table with fields as below:
#subjects
#communication_medium
#sender
#recipients
#cc
#bcc
#phone_no
#delivery_status
#content
#text_content
#communication_type
#comment_type
#status
#sent_or_received
#additional_info
#communication_date
#read_receipt
#sender_full_name
#read_by_recipient
#read_by_recipient_on
#reference_doctype forigen key on document type
#reference_name
#reference_owner readonly field
#email_account link email account
#in_reply_to forigen key to Communication
#user
#unread_notification_sent
#seen
#_User_tags
#email_inbox
#email_status
#has_attachment
#rating intiger type
#feedback_request
#timeline_links
#imap_folder
class Communication(models.Model):
    subjects = models.CharField(max_length=255, blank=True, null=True)
    communication_medium = models.CharField(max_length=255, blank=True, null=True)
    sender = models.CharField(max_length=255, blank=True, null=True)
    recipients = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    bcc = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=255, blank=True, null=True)
    delivery_status = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    communication_type = models.CharField(max_length=255, blank=True, null=True)
    comment_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sent_or_received = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    communication_date = models.DateTimeField(blank=True, null=True)
    read_receipt = models.CharField(max_length=255, blank=True, null=True)
    sender_full_name = models.CharField(max_length=255, blank=True, null=True)
    read_by_recipient = models.CharField(max_length=255, blank=True, null=True)
    read_by_recipient_on = models.DateTimeField(blank=True, null=True)
    reference_doctype = models.ForeignKey(Doctype, on_delete=CASCADE, blank=True, null=True)
    reference_name = models.CharField(max_length=255, blank=True, null=True)
    reference_owner = models.CharField(max_length=255, blank=True, null=True)
    # email_account = models.ForeignKey('email_account', on_delete=CASCADE, blank=True, null=True)
    in_reply_to = models.ForeignKey("Communication", on_delete=CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    unread_notification_sent = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    _User_tags = models.CharField(max_length=255, blank=True, null=True)
    # email_inbox = models.ForeignKey('email_inbox', on_delete=CASCADE, blank=True, null=True)
    email_status = models.CharField(max_length=255, blank=True, null=True)
    has_attachment = models.BooleanField(default=False)
    rating = models.IntegerField(blank=True, null=True)
    feedback_request = models.BooleanField(default=False)
    timeline_links = models.CharField(max_length=255, blank=True, null=True)
    imap_folder = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication'


    def __str__(self):
        return self.subjects


#email_account -fk
#email_inbox -fk