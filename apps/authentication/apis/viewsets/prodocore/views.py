from requests import Response
from rest_framework import viewsets,permissions

#modules
from apps.prodocore.models import Member, Group, GroupType, GroupEntity, GroupMember, GroupMemberRole    

#serializers
from apps.authentication.serializers.prodocore.serializer import MemberSerializer, GroupSerializer, GroupTypeSerializer, GroupEntitySerializer, GroupMemberSerializer, GroupMemberRoleSerializer    

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupTypeViewSet(viewsets.ModelViewSet):
    queryset = GroupType.objects.all()
    serializer_class = GroupTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupEntityViewSet(viewsets.ModelViewSet):
    queryset = GroupEntity.objects.all()
    serializer_class = GroupEntitySerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupMemberViewSet(viewsets.ModelViewSet):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupMemberRoleViewSet(viewsets.ModelViewSet):
    queryset = GroupMemberRole.objects.all()
    serializer_class = GroupMemberRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupMemberRoleViewSet(viewsets.ModelViewSet):
    queryset = GroupMemberRole.objects.all()
    serializer_class = GroupMemberRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

 


