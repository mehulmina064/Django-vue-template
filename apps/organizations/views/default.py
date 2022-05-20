# -*- coding: utf-8 -*-

# from apps.authentication.apis.viewsets import organizations
from apps.organizations.models import Organization
from apps.organizations.views.base import ViewFactory
from apps.organizations.views.mixins import AdminRequiredMixin
from apps.organizations.views.mixins import MembershipRequiredMixin
from apps.organizations.views.mixins import OwnerRequiredMixin

bases = ViewFactory(Organization)


class OrganizationList(bases.OrganizationList):
    
    pass


class OrganizationCreate(bases.OrganizationCreate):
    """
    Allows any user to create a new organization.
    """

    pass


class OrganizationDetail(MembershipRequiredMixin, bases.OrganizationDetail):
    pass


class OrganizationUpdate(AdminRequiredMixin, bases.OrganizationUpdate):
    pass


class OrganizationDelete(OwnerRequiredMixin, bases.OrganizationDelete):
    pass


class OrganizationUserList(MembershipRequiredMixin, bases.OrganizationUserList):
    pass


class OrganizationUserDetail(AdminRequiredMixin, bases.OrganizationUserDetail):
    pass


class OrganizationUserUpdate(AdminRequiredMixin, bases.OrganizationUserUpdate):
    pass


class OrganizationUserCreate(AdminRequiredMixin, bases.OrganizationUserCreate):
    pass


class OrganizationUserRemind(AdminRequiredMixin, bases.OrganizationUserRemind):
    pass


class OrganizationUserDelete(AdminRequiredMixin, bases.OrganizationUserDelete):
    pass

