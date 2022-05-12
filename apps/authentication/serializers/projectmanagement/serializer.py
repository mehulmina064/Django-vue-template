from rest_framework import serializers

from apps.projectmanagement.models import ActivityCost, ActivityType,DependentTask,ProjectTemplateTask,ProjectTemplate,ProjectType,ProjectUpdate,ProjectUser,Project,TaskDependsOn,TaskType,Task,TimesheetDetail,TimeSheet



class ActivityCostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityCost
        fields = '__all__'
        
class ActivityTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityType
        fields = '__all__'
    
class DependentTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DependentTask
        fields = '__all__'
        
class ProjectTemplateTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectTemplateTask
        fields = '__all__'
        
class ProjectTemplateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectTemplate
        fields = '__all__'
        
class ProjectTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectType
        fields = '__all__'
        
class ProjectUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectUpdate
        fields = '__all__'
        
class ProjectUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProjectUser
        fields = '__all__'
        
class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
        
class TaskDependsOnSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskDependsOn
        fields = '__all__'
        
class TaskTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskType
        fields = '__all__'
    
   
class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
        
   
class TimesheetDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TimesheetDetail
        fields = '__all__'
        
   
class TimeSheetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TimeSheet
        fields = '__all__'
        
   