from django.db import models
from django.db.models.signals import post_save, post_delete

from organizations.abstract import AbstractOrganization
from organizations.abstract import AbstractOrganizationInvitation
from organizations.abstract import AbstractOrganizationOwner
from organizations.abstract import AbstractOrganizationUser
from apps.prodocore.models import Member,Group,GroupMemberRoleMixin,GroupEntityMixin,GroupMemberRoleMixin,GroupMemberMixin,\
    GroupMixin,MemberMixin, group_save, group_delete, member_save, member_delete, group_member_save, group_member_delete, \
    DjangoUser, DjangoGroup

class Organization(AbstractOrganization):
    """
    Default Organization model
    """

    class Meta(AbstractOrganization.Meta):
        abstract = False
    
    

class OrganizationUser(AbstractOrganizationUser):
    """
    Default OrganizationUser model.
    """

    class Meta(AbstractOrganizationUser.Meta):
        abstract = False


class OrganizationOwner(AbstractOrganizationOwner):
    """
    Default OrganizationOwner model.
    """

    class Meta(AbstractOrganizationOwner.Meta):
        abstract = False


class OrganizationInvitation(AbstractOrganizationInvitation):
    class Meta(AbstractOrganizationInvitation.Meta):
        abstract = False
             
class OrganizationMember(Member):
    """
    Default OrganizationUser model.
    """
    
    class Meta:
        abstract = False
        

   
class OrganizationMemberSubclass(Member):
    phone_number = models.CharField(max_length=20)
    
    class Meta:
        abstract = False
        
class Department(Organization):
    dep_name = models.CharField(max_length=50)
    dep_no = models.CharField(max_length=50, default="")
    
    class Meta:
        abstract = False
    
class Team(Organization):
    dep = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    team_name = models.CharField(max_length=50)
    team_no = models.CharField(max_length=50, default="")
    
    class Meta:
        abstract = False
    

        







    

    
    



