
from rest_framework import routers
from django.urls import  path,include

#import organization views
from apps.authentication.apis.viewsets.organizations.views import OrganizationViewSet, OrganizationUserViewSet, OrganizationOwnerViewSet, OrganizationInvitationViewSet, OrganizationMemberViewSet, OrganizationMemberSubclassViewSet, DepartmentViewSet, TeamViewSet

#import account views
from apps.authentication.apis.viewsets.account.views import AccountUserViewSet,AccountViewSet

#import prodocore views
from apps.authentication.apis.viewsets.prodocore.views import MemberViewSet,GroupViewSet,GroupTypeViewSet,GroupEntityViewSet,GroupMemberViewSet,GroupMemberRoleViewSet

#import projectmanagement views
from apps.authentication.apis.viewsets.projectmanagement.views import ActivityCostViewSet,ActivityTypeViewSet,DependentTaskViewSet,ProjectTemplateTaskViewSet,ProjectTemplateViewSet,ProjectTypeViewSet,ProjectUpdateViewSet,ProjectUserViewSet,ProjectViewSet,TaskDependsOnViewSet,TaskTypeViewSet,TaskViewSet,TimesheetDetailViewSet,TimeSheetViewSet


#import core views
from apps.authentication.apis.viewsets.core.views import Access_LogViewSet,Activity_LogViewSet,DoctypeViewSet,Block_ModuleViewSet,\
    CommentViewSet,CommunicationViewSet,Communication_LinkViewSet,Communication_DocpermViewSet,Data_ImportViewSet,\
    Data_ExportViewSet,Data_Import_LogViewSet,DefaultValueViewSet,Deleted_DocumentViewSet,DocfieldViewSet,DocshareViewSet,\
    Doctype_ActionViewSet,Doctype_LinkViewSet,Doctype_StateViewSet,DomainViewSet,Domain_SettingsViewSet,Dynamic_LinkViewSet,\
    Error_LogViewSet,Error_SnapshotViewSet,FeedbackViewSet,FileViewSet,Has_DomainViewSet,Has_RoleViewSet,\
    Install_ApplicationViewSet,LanguageViewSet,Log_Setting_UserViewSet,Log_SettingsViewSet,Module_DefViewSet,Module_ProfileViewSet,\
    Navbar_ItemViewSet,Navbar_SettingsViewSet,PackageViewSet,PageViewSet,Payment_GatewayViewSet,Prepared_ReportViewSet,\
    Report_ColumnViewSet,Report_FilterViewSet,ReportViewSet,Role_ProfileViewSet,RoleViewSet,Scheduled_Job_LogViewSet,\
    Scheduled_Job_TypeViewSet,Server_ScriptViewSet,Session_DefaultViewSet,Sms_ParameterViewSet,Sms_SettingsViewSet,\
    Success_ActionViewSet,System_SettingsViewSet,TestViewSet,Transaction_LogViewSet,TranslationViewSet,UserDocument_TypeViewSet,\
    UserEmailViewSet,UserGroupViewSet,UserGroup_MemberViewSet,UserGroupViewSet,UserGroup_MemberViewSet,UserViewSet



router = routers.DefaultRouter()

#paths of organization application
router.register(r'org', OrganizationViewSet)
router.register(r'orguser', OrganizationUserViewSet)
router.register(r'orgowner', OrganizationOwnerViewSet)
router.register(r'orginvitation',OrganizationInvitationViewSet)
router.register(r'orgmember',OrganizationMemberViewSet)
router.register(r'orgmembersubclass',OrganizationMemberSubclassViewSet)
router.register(r'dep',DepartmentViewSet)
router.register(r'team',TeamViewSet)

#paths of account application
router.register(r'Account', AccountViewSet)
router.register(r'AccountUser', AccountUserViewSet)
#paths of prodocore 
router.register(r'member', MemberViewSet)
router.register(r'group', GroupViewSet)
router.register(r'grouptype', GroupTypeViewSet)
router.register(r'groupentity', GroupEntityViewSet)
router.register(r'groupmember', GroupMemberViewSet)
router.register(r'groupmemberrole', GroupMemberRoleViewSet)

#paths of projectmanagement application
# router.register(r' ', ActivityCostViewSet)
router.register(r'activitytype', ActivityTypeViewSet)
router.register(r'dependenttask', DependentTaskViewSet)
router.register(r'projecttemplatetask', ProjectTemplateTaskViewSet)
router.register(r'projecttemplate', ProjectTemplateViewSet)
router.register(r'projecttype', ProjectTypeViewSet)
router.register(r'projectupdate', ProjectUpdateViewSet)
router.register(r'projectuser', ProjectUserViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'taskdependson', TaskDependsOnViewSet)
router.register(r'tasktype', TaskTypeViewSet)
router.register(r'task', TaskViewSet)
router.register(r'timesheetdetail', TimesheetDetailViewSet)
router.register(r'timesheet', TimeSheetViewSet)


#paths of core application
router.register(r'access_log', Access_LogViewSet)
router.register(r'activity_log', Activity_LogViewSet)
router.register(r'doctype', DoctypeViewSet)
router.register(r'block_module', Block_ModuleViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'communication', CommunicationViewSet)
router.register(r'communication_link', Communication_LinkViewSet)
router.register(r'communication_docperm', Communication_DocpermViewSet)
router.register(r'data_import', Data_ImportViewSet)
router.register(r'data_export', Data_ExportViewSet)
router.register(r'data_import_log', Data_Import_LogViewSet)
router.register(r'defaultvalue', DefaultValueViewSet)
router.register(r'deleted_document', Deleted_DocumentViewSet)
router.register(r'docfield', DocfieldViewSet)
router.register(r'docshare', DocshareViewSet)
router.register(r'doctype_action', Doctype_ActionViewSet)
router.register(r'doctype_link', Doctype_LinkViewSet)
router.register(r'doctype_state', Doctype_StateViewSet)
router.register(r'domain', DomainViewSet)
router.register(r'domain_settings', Domain_SettingsViewSet)
router.register(r'dynamic_link', Dynamic_LinkViewSet)
router.register(r'error_log', Error_LogViewSet)
router.register(r'error_snapshot', Error_SnapshotViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'file', FileViewSet)
router.register(r'has_domain', Has_DomainViewSet)
router.register(r'has_role', Has_RoleViewSet)
router.register(r'install_application', Install_ApplicationViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'log_setting_user', Log_Setting_UserViewSet)
router.register(r'log_settings', Log_SettingsViewSet)
router.register(r'module_def', Module_DefViewSet)
router.register(r'module_profile', Module_ProfileViewSet)
router.register(r'navbar_item', Navbar_ItemViewSet)
router.register(r'navbar_settings', Navbar_SettingsViewSet)
router.register(r'package', PackageViewSet)
router.register(r'page', PageViewSet)
router.register(r'payment_gateway', Payment_GatewayViewSet)
router.register(r'prepared_report', Prepared_ReportViewSet)
router.register(r'report_column', Report_ColumnViewSet)
router.register(r'report_filter', Report_FilterViewSet)
router.register(r'report', ReportViewSet)
router.register(r'role_profile', Role_ProfileViewSet)
router.register(r'role', RoleViewSet)
router.register(r'scheduled_job_log', Scheduled_Job_LogViewSet)
router.register(r'scheduled_job_type', Scheduled_Job_TypeViewSet)
router.register(r'server_script', Server_ScriptViewSet)
router.register(r'session_default', Session_DefaultViewSet)
router.register(r'sms_parameter', Sms_ParameterViewSet)
router.register(r'sms_settings', Sms_SettingsViewSet)
router.register(r'success_action', Success_ActionViewSet)
router.register(r'system_settings', System_SettingsViewSet)
router.register(r'test', TestViewSet)
router.register(r'transaction_log', Transaction_LogViewSet)
router.register(r'translation', TranslationViewSet)
router.register(r'userdocument_type', UserDocument_TypeViewSet)
router.register(r'useremail', UserEmailViewSet)
router.register(r'usergroup', UserGroupViewSet)
router.register(r'usergroup_member', UserGroup_MemberViewSet)
router.register(r'usergroup', UserGroupViewSet)
router.register(r'usergroup_member', UserGroup_MemberViewSet)
router.register(r'user', UserViewSet)




urlpatterns = [
    path('/', include(router.urls)),
   
]

