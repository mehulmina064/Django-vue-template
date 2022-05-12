from typing_extensions import Self
from xml.dom.minidom import DocumentType
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from .role import Role

#create communication_docperm table with fields as below:
#role forigen key to Role
#permlevel intiger type
#read boolean type
#write boolean type
#create boolean type
#delete boolean type
#submit boolean type
#cancel boolean type
#amend boolean type
#report boolean type default false
#export boolean type default true
#import boolean type default false
#set_User_permissions boolean type default false
#share boolean type default false
#print boolean type default false
#email boolean type default false
#parent char type
#select boolean type default false
class Communication_Docperm(models.Model):
    role = models.ForeignKey(Role, on_delete=CASCADE, blank=True, null=True)
    permlevel = models.IntegerField(blank=True, null=True)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    create = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    submit = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    amend = models.BooleanField(default=False)
    report = models.BooleanField(default=False)
    export = models.BooleanField(default=True)
    Import = models.BooleanField(default=False)
    set_User_permissions = models.BooleanField(default=False)
    share = models.BooleanField(default=False)
    print = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    parent = models.CharField(max_length=150, blank=True, null=True)
    select = models.BooleanField(default=False)
    def __str__(self):
        return self.role
    class Meta:
        verbose_name_plural = "Communication_Docperm"
