from rest_framework import serializers
from apps.organizations.models import Organization, OrganizationUser, OrganizationOwner, OrganizationInvitation, OrganizationMember, OrganizationMemberSubclass, Department, Team

class OrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organization
        fields = '__all__' 
        
class OrganizationUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrganizationUser
        fields = '__all__' 
        
class OrganizationOwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrganizationOwner
        fields = '__all__' 
        
class OrganizationInvitationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrganizationInvitation
        fields = '__all__' 
        
class OrganizationMemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrganizationMember
        fields = '__all__' 
        
class OrganizationMemberSubclassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrganizationMemberSubclass
        fields = '__all__' 
        
class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = '__all__' 
        
class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = '__all__' 
        
