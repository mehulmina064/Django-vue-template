from rest_framework import viewsets,permissions
from apps.organizations.models import Organization, OrganizationUser, OrganizationOwner, OrganizationInvitation, OrganizationMember, OrganizationMemberSubclass, Department, Team
from apps.authentication.serializers.organizations.serializer import OrganizationSerializer, OrganizationUserSerializer, OrganizationOwnerSerializer, OrganizationInvitationSerializer, OrganizationMemberSerializer, OrganizationMemberSubclassSerializer, DepartmentSerializer, TeamSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrganizationUserViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrganizationOwnerViewSet(viewsets.ModelViewSet):
    queryset = OrganizationOwner.objects.all()
    serializer_class = OrganizationOwnerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrganizationInvitationViewSet(viewsets.ModelViewSet):
    queryset = OrganizationInvitation.objects.all()
    serializer_class = OrganizationInvitationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrganizationMemberViewSet(viewsets.ModelViewSet):
    queryset = OrganizationMember.objects.all()
    serializer_class = OrganizationMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrganizationMemberSubclassViewSet(viewsets.ModelViewSet):
    queryset = OrganizationMemberSubclass.objects.all()
    serializer_class = OrganizationMemberSubclassSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]