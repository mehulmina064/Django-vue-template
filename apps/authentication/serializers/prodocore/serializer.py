from rest_framework import serializers
from apps.prodocore.models import Member, Group, GroupType, GroupEntity, GroupMember, GroupMemberRole

#create serializer for Member
class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = '__all__'

#create serializer for Group
class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'

#create serializer for GroupType
class GroupTypeSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = GroupType
        fields = '__all__'

#create serializer for GroupEntity
class GroupEntitySerializer(serializers.ModelSerializer):
            
    class Meta:
        model = GroupEntity
        fields = '__all__'

#create serializer for GroupMember
class GroupMemberSerializer(serializers.ModelSerializer):
                    
    class Meta:
        model = GroupMember
        fields = '__all__'

#create serializer for GroupMemberRole
class GroupMemberRoleSerializer(serializers.ModelSerializer):
                            
    class Meta:
        model = GroupMemberRole
        fields = '__all__'