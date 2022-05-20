
from rest_framework import routers
from django.urls import  path,include

#import organization views
from apps.authentication.apis.viewsets.organizations.views import OrganizationViewSet, OrganizationUserViewSet, OrganizationOwnerViewSet, OrganizationInvitationViewSet, OrganizationMemberViewSet, OrganizationMemberSubclassViewSet, DepartmentViewSet, TeamViewSet
from apps.organizations.views.default import OrganizationList,OrganizationCreate,OrganizationDetail,OrganizationUpdate,OrganizationDelete,OrganizationUserList,OrganizationUserDetail,OrganizationUserCreate,OrganizationUserDelete,OrganizationUserUpdate,OrganizationUserRemind
#import account views
#import core views


#paths of organization application
# router.register(r'org', OrganizationViewSet)
# router.register(r'orguser', OrganizationUserViewSet)
# router.register(r'orgowner', OrganizationOwnerViewSet)
# router.register(r'orginvitation',OrganizationInvitationViewSet)
# router.register(r'orgmember',OrganizationMemberViewSet)
# router.register(r'orgmembersubclass',OrganizationMemberSubclassViewSet)
# router.register(r'dep',DepartmentViewSet)
# router.register(r'team',TeamViewSet)
#paths for organizion views
# router.register(r'org', OrganizationList)
# router.register(r'orgcreate', OrganizationCreate)
# router.register(r'orgdetail', OrganizationDetail)
# router.register(r'orgupdate', OrganizationUpdate)
# router.register(r'orgdelete', OrganizationDelete)
# router.register(r'orguser', OrganizationUserList)
# router.register(r'orguserdetail', OrganizationUserDetail)
# router.register(r'orgusercreate', OrganizationUserCreate)
# router.register(r'orguserdelete', OrganizationUserDelete)
# router.register(r'orguserremind', OrganizationUserRemind)
# router.register(r'orguserupdate', OrganizationUserUpdate)

#paths of account applicatio


urlpatterns = [
    path('org/', OrganizationList.as_view(),name="organization_list"),
    path('orgcreate/', OrganizationCreate.as_view(),name="organization_add"),
    path('orgdetail/<int:pk>/', OrganizationDetail.as_view(),name="organization_detail"),
    path('orgupdate/<int:pk>/', OrganizationUpdate.as_view(),name="organization_edit"),
    path('orgdelete/<int:pk>/', OrganizationDelete.as_view(),name="organization_delete"),
    path('orguser/', OrganizationUserList.as_view(),name="organization_user_list"),
    path('orguserdetail/<int:pk>/', OrganizationUserDetail.as_view(),name="organization_user_detail"),
    path('orgusercreate/', OrganizationUserCreate.as_view(),name="organization_user_add"),
    path('orguserdelete/<int:pk>/', OrganizationUserDelete.as_view(),name="organization_user_delete"),
    path('orguserremind/<int:pk>/', OrganizationUserRemind.as_view(),name="organization_user_remind"),
    path('orguserupdate/<int:pk>/', OrganizationUserUpdate.as_view(),name="organization_user_edit"),
    # path('org/', BookListView.as_view(), name='organization'),

]

