from rest_framework import viewsets,permissions
from apps.projectmanagement.models import ActivityCost, ActivityType,DependentTask,ProjectTemplateTask,ProjectTemplate,ProjectType,ProjectUpdate,ProjectUser,Project,TaskDependsOn,TaskType,Task,TimesheetDetail,TimeSheet
from apps.authentication.serializers.projectmanagement.serializer import ActivityCostSerializer, ActivityTypeSerializer,DependentTaskSerializer,ProjectTemplateTaskSerializer,ProjectTemplateSerializer,ProjectTypeSerializer,ProjectUpdateSerializer,ProjectUserSerializer,ProjectSerializer,TaskDependsOnSerializer,TaskTypeSerializer,TaskSerializer,TimesheetDetailSerializer,TimeSheetSerializer

class ActivityCostViewSet(viewsets.ModelViewSet):
    queryset = ActivityCost.objects.all()
    serializer_class = ActivityCostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DependentTaskViewSet(viewsets.ModelViewSet):
    queryset = DependentTask.objects.all()
    serializer_class = DependentTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectTemplateTaskViewSet(viewsets.ModelViewSet):
    queryset = ProjectTemplateTask.objects.all()
    serializer_class = ProjectTemplateTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectTemplateViewSet(viewsets.ModelViewSet):
    queryset = ProjectTemplate.objects.all()
    serializer_class = ProjectTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectUpdateViewSet(viewsets.ModelViewSet):
    queryset = ProjectUpdate.objects.all()
    serializer_class = ProjectUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TaskDependsOnViewSet(viewsets.ModelViewSet):
    queryset = TaskDependsOn.objects.all()
    serializer_class = TaskDependsOnSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TaskTypeViewSet(viewsets.ModelViewSet):
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TimesheetDetailViewSet(viewsets.ModelViewSet):
    queryset = TimesheetDetail.objects.all()
    serializer_class = TimesheetDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TimeSheetViewSet(viewsets.ModelViewSet):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
