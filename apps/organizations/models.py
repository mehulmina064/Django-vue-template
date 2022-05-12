from django.db import models
from django.db.models.signals import post_save, post_delete

from organizations.abstract import AbstractOrganization
from organizations.abstract import AbstractOrganizationInvitation
from organizations.abstract import AbstractOrganizationOwner
from organizations.abstract import AbstractOrganizationUser
from apps.prodocore.models import Member,GroupType,GroupMemberRoleMixin,GroupEntityMixin,GroupMemberRoleMixin,GroupMemberMixin,\
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
        


"mixin models"

# def organization_with_mixin_get_auth_models_sync_func(instance):
#     return True


# class OrganizationMemberRoleWithMixin(GroupMemberRoleMixin):

#     class Meta:
#         abstract = False


# class OrganizationEntityWithMixin(GroupEntityMixin):

#     class Meta:
#         abstract = False


# class OrganizationTypeWithMixin(GroupMemberRoleMixin):

#     class Meta:
#         abstract = False


# class OrganizationGroupMemberWithMixin(GroupMemberMixin):
#     group = models.ForeignKey('OrganizationGroupWithMixin', related_name='group_membership',
#                               on_delete=models.CASCADE)
#     member = models.ForeignKey('OrganizationMemberWithMixin', related_name='group_membership',
#                                on_delete=models.CASCADE)
#     roles = models.ManyToManyField(OrganizationMemberRoleWithMixin, blank=True)
#     expiration_date = models.DateTimeField(null=True, default=None)


# def organization_group_member_save(*args, **kwargs):
#     group_member_save(*args, get_auth_models_sync_func=organization_with_mixin_get_auth_models_sync_func, **kwargs)


# def organization_group_member_delete(*args, **kwargs):
#     group_member_delete(*args, get_auth_models_sync_func=organization_with_mixin_get_auth_models_sync_func, **kwargs)


# class OrganizationGroupWithMixin(GroupMixin):
#     last_edit_date = models.DateTimeField(auto_now=True, null=True)
#     short_name = models.CharField(max_length=50, default='', blank=True)
#     city = models.CharField(max_length=200, blank=True, default='')

#     group_type = models.ForeignKey(GroupType, null=True, blank=True, on_delete=models.SET_NULL,
#                                    related_name='%(app_label)s_%(class)s_set')
#     group_entities = models.ManyToManyField(OrganizationEntityWithMixin, blank=True,
#                                             related_name='%(app_label)s_%(class)s_set')

#     django_group = models.ForeignKey(DjangoGroup, null=True, blank=True, on_delete=models.SET_NULL)
#     group_members = models.ManyToManyField('OrganizationMemberWithMixin', through=OrganizationGroupMemberWithMixin,
#                                            through_fields=('group', 'member'),
#                                            related_name='%(app_label)s_%(class)s_set')

#     class GroupsManagerMeta:
#         member_model = 'testproject.OrganizationMemberWithMixin'
#         group_member_model = 'testproject.OrganizationGroupMemberWithMixin'

#     def save(self, *args, **kwargs):
#         if not self.short_name:
#             self.short_name = self.name
#         super(OrganizationGroupWithMixin, self).save(*args, **kwargs)

#     @property
#     def members_names(self):
#         return [member.full_name for member in self.group_members.all()]


# post_save.connect(group_save, sender=OrganizationGroupWithMixin)
# post_delete.connect(group_delete, sender=OrganizationGroupWithMixin)


# class OrganizationMemberWithMixin(MemberMixin):
#     last_edit_date = models.DateTimeField(auto_now=True, null=True)

#     django_user = models.ForeignKey(DjangoUser, null=True, blank=True, on_delete=models.SET_NULL,
#                                     related_name='%(app_label)s_%(class)s_set')

#     class GroupsManagerMeta:
#         group_model = 'testproject.OrganizationGroupWithMixin'
#         group_member_model = 'testproject.OrganizationGroupMemberWithMixin'

#     def __unicode__(self):
#         if self.email:
#             return '%s (%s)' % (self.full_name, self.email)
#         return self.full_name

#     def __str__(self):
#         if self.email:
#             return '%s (%s)' % (self.full_name, self.email)
#         return self.full_name


# post_save.connect(member_save, sender=OrganizationMemberWithMixin)
# post_delete.connect(member_delete, sender=OrganizationMemberWithMixin)


# post_save.connect(organization_group_member_save, sender=OrganizationGroupMemberWithMixin)
# post_delete.connect(organization_group_member_delete, sender=OrganizationGroupMemberWithMixin)



