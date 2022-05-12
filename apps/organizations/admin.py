from django.contrib import admin

from apps.organizations import models as models


admin.site.register(models.Organization)
admin.site.register(models.OrganizationUser)
admin.site.register(models.OrganizationMember)
admin.site.register(models.OrganizationMemberSubclass)
admin.site.register(models.OrganizationOwner)
admin.site.register(models.OrganizationInvitation)





