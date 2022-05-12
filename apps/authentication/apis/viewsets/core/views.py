from requests import Response
from rest_framework import viewsets,permissions

#modules
from apps.core.models.access_log import Access_Log
from apps.core.models.activity_log import Activity_Log
from apps.core.models.doctype import Doctype
from apps.core.models.block_module import Block_Module
from apps.core.models.comment import Comment
from apps.core.models.communication import Communication
from apps.core.models.communication_link import Communication_Link
from apps.core.models.custom_docperm import Communication_Docperm
from apps.core.models.data_import import Data_Import
from apps.core.models.data_export import Data_Export
from apps.core.models.data_import_log import Data_Import_Log
from apps.core.models.defaultvalue import DefaultValue
from apps.core.models.deleted_document import Deleted_Document
from apps.core.models.docfield import Docfield
from apps.core.models.docshare import Docshare
from apps.core.models.doctype_action import Doctype_Action
from apps.core.models.doctype_link import Doctype_Link
from apps.core.models.doctype_state import Doctype_State
from apps.core.models.domain import Domain
from apps.core.models.domain_settings import Domain_Settings
from apps.core.models.dynamic_link import Dynamic_Link
from apps.core.models.error_log import Error_Log
from apps.core.models.error_snapshot import Error_Snapshot
from apps.core.models.feedback import Feedback
from apps.core.models.file import File
from apps.core.models.has_domain import Has_Domain
from apps.core.models.has_role import Has_Role
from apps.core.models.installed_application import Install_Application
from apps.core.models.language import Language
from apps.core.models.log_setting_user import Log_Setting_User
from apps.core.models.log_settings import Log_Settings
from apps.core.models.module_def import Module_Def
from apps.core.models.module_profile import Module_Profile
from apps.core.models.navbar_item import Navbar_Item
from apps.core.models.navbar_settings import Navbar_Settings
from apps.core.models.package import Package
from apps.core.models.page import Page
from apps.core.models.payment_gateway import Payment_Gateway
from apps.core.models.prepared_report import Prepared_Report
from apps.core.models.report_column import Report_Column
from apps.core.models.report_filter import Report_Filter
from apps.core.models.report import Report
from apps.core.models.role_profile import Role_Profile
from apps.core.models.role import Role
from apps.core.models.scheduled_job_log import Scheduled_Job_Log
from apps.core.models.scheduled_job_type import Scheduled_Job_Type
from apps.core.models.server_script import Server_Script
from apps.core.models.session_default import Session_Default
from apps.core.models.sms_parameter import Sms_Parameter
from apps.core.models.sms_settings import Sms_Settings
from apps.core.models.success_action import Success_Action
from apps.core.models.system_settings import System_Settings
from apps.core.models.test import Test
from apps.core.models.transaction_log import Transaction_Log
from apps.core.models.translation import Translation
from apps.core.models.user_document_type import UserDocument_Type
from apps.core.models.user_email import UserEmail
from apps.core.models.user_group import UserGroup
from apps.core.models.user_group_member import UserGroup_Member
from apps.core.models.user_select_document_type import UserSelect_Document_Type
from apps.core.models.user_social_login import UserSocial_Login
from apps.core.models.user_type_module import UserType_Module
from apps.core.models.user_type import UserType
from apps.core.models.user import User
from apps.core.models.version import Version

#serializers
from apps.authentication.serializers.core.serializer import Access_LogSerializer,Activity_LogSerializer,DoctypeSerializer, \
    Block_ModuleSerializer,CommentSerializer,CommunicationSerializer,Communication_LinkSerializer,Communication_DocpermSerializer, \
    Data_ImportSerializer,Data_ExportSerializer,Data_Import_LogSerializer,DefaultValueSerializer, \
    Deleted_DocumentSerializer,DocfieldSerializer,DocshareSerializer,Doctype_ActionSerializer, \
    Doctype_LinkSerializer,Doctype_StateSerializer,DomainSerializer,Domain_SettingsSerializer, \
    Dynamic_LinkSerializer,Error_LogSerializer,Error_SnapshotSerializer,FeedbackSerializer, \
    FileSerializer,Has_DomainSerializer,Has_RoleSerializer,Install_ApplicationSerializer,LanguageSerializer, \
    Log_Setting_UserSerializer,Log_SettingsSerializer,Module_DefSerializer,Module_ProfileSerializer, \
    Navbar_ItemSerializer,Navbar_SettingsSerializer,PackageSerializer,PageSerializer, \
    Payment_GatewaySerializer,Prepared_ReportSerializer,Report_ColumnSerializer,Report_FilterSerializer, \
    ReportSerializer,Role_ProfileSerializer,RoleSerializer,Scheduled_Job_LogSerializer,Scheduled_Job_TypeSerializer, \
    Server_ScriptSerializer,Session_DefaultSerializer,Sms_ParameterSerializer,Sms_SettingsSerializer, \
    Success_ActionSerializer,System_SettingsSerializer,TestSerializer,Transaction_LogSerializer, \
    TranslationSerializer,UserDocument_TypeSerializer,UserEmailSerializer,UserGroupSerializer,UserGroup_MemberSerializer, \
    UserSelect_Document_TypeSerializer,UserSocial_LoginSerializer,UserType_ModuleSerializer, \
    UserTypeSerializer,UserSerializer,VersionSerializer


#create api views for core models
class Access_LogViewSet(viewsets.ModelViewSet):
    queryset = Access_Log.objects.all()
    serializer_class = Access_LogSerializer
    permission_classes = [permissions.IsAuthenticated]

class Activity_LogViewSet(viewsets.ModelViewSet):
    queryset = Activity_Log.objects.all()
    serializer_class = Activity_LogSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctypeViewSet(viewsets.ModelViewSet):
    queryset = Doctype.objects.all()
    serializer_class = DoctypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class Block_ModuleViewSet(viewsets.ModelViewSet):
    queryset = Block_Module.objects.all()
    serializer_class = Block_ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAuthenticated]

class Communication_LinkViewSet(viewsets.ModelViewSet):
    queryset = Communication_Link.objects.all()
    serializer_class = Communication_LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class Communication_DocpermViewSet(viewsets.ModelViewSet):
    queryset = Communication_Docperm.objects.all()
    serializer_class = Communication_DocpermSerializer
    permission_classes = [permissions.IsAuthenticated]

class Data_ImportViewSet(viewsets.ModelViewSet):
    queryset = Data_Import.objects.all()
    serializer_class = Data_ImportSerializer
    permission_classes = [permissions.IsAuthenticated]

class Data_ExportViewSet(viewsets.ModelViewSet):
    queryset = Data_Export.objects.all()
    serializer_class = Data_ExportSerializer
    permission_classes = [permissions.IsAuthenticated]

class Data_Import_LogViewSet(viewsets.ModelViewSet):
    queryset = Data_Import_Log.objects.all()
    serializer_class = Data_Import_LogSerializer
    permission_classes = [permissions.IsAuthenticated]

class DefaultValueViewSet(viewsets.ModelViewSet):
    queryset = DefaultValue.objects.all()
    serializer_class = DefaultValueSerializer
    permission_classes = [permissions.IsAuthenticated]

class Deleted_DocumentViewSet(viewsets.ModelViewSet):
    queryset = Deleted_Document.objects.all()
    serializer_class = Deleted_DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class DocfieldViewSet(viewsets.ModelViewSet):
    queryset = Docfield.objects.all()
    serializer_class = DocfieldSerializer
    permission_classes = [permissions.IsAuthenticated]

class DocshareViewSet(viewsets.ModelViewSet):
    queryset = Docshare.objects.all()
    serializer_class = DocshareSerializer
    permission_classes = [permissions.IsAuthenticated]

class Doctype_ActionViewSet(viewsets.ModelViewSet):
    queryset = Doctype_Action.objects.all()
    serializer_class = Doctype_ActionSerializer
    permission_classes = [permissions.IsAuthenticated]

class Doctype_LinkViewSet(viewsets.ModelViewSet):
    queryset = Doctype_Link.objects.all()
    serializer_class = Doctype_LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class Doctype_StateViewSet(viewsets.ModelViewSet):
    queryset = Doctype_State.objects.all()
    serializer_class = Doctype_StateSerializer
    permission_classes = [permissions.IsAuthenticated]

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [permissions.IsAuthenticated]

class Domain_SettingsViewSet(viewsets.ModelViewSet):
    queryset = Domain_Settings.objects.all()
    serializer_class = Domain_SettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Dynamic_LinkViewSet(viewsets.ModelViewSet):
    queryset = Dynamic_Link.objects.all()
    serializer_class = Dynamic_LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class Error_LogViewSet(viewsets.ModelViewSet):
    queryset = Error_Log.objects.all()
    serializer_class = Error_LogSerializer
    permission_classes = [permissions.IsAuthenticated]

class Error_SnapshotViewSet(viewsets.ModelViewSet):
    queryset = Error_Snapshot.objects.all()
    serializer_class = Error_SnapshotSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

class Has_DomainViewSet(viewsets.ModelViewSet):
    queryset = Has_Domain.objects.all()
    serializer_class = Has_DomainSerializer
    permission_classes = [permissions.IsAuthenticated]

class Has_RoleViewSet(viewsets.ModelViewSet):
    queryset = Has_Role.objects.all()
    serializer_class = Has_RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class Install_ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Install_Application.objects.all()
    serializer_class = Install_ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]

class Log_SettingsViewSet(viewsets.ModelViewSet):
    queryset = Log_Settings.objects.all()
    serializer_class = Log_SettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Log_Setting_UserViewSet(viewsets.ModelViewSet):
    queryset = Log_Setting_User.objects.all()
    serializer_class = Log_Setting_UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class Module_DefViewSet(viewsets.ModelViewSet):
    queryset = Module_Def.objects.all()
    serializer_class = Module_DefSerializer
    permission_classes = [permissions.IsAuthenticated]

class Module_ProfileViewSet(viewsets.ModelViewSet):
    queryset = Module_Profile.objects.all()
    serializer_class = Module_ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class Navbar_SettingsViewSet(viewsets.ModelViewSet):
    queryset = Navbar_Settings.objects.all()
    serializer_class = Navbar_SettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Navbar_ItemViewSet(viewsets.ModelViewSet):
    queryset = Navbar_Item.objects.all()
    serializer_class = Navbar_ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticated]

class Payment_GatewayViewSet(viewsets.ModelViewSet):
    queryset = Payment_Gateway.objects.all()
    serializer_class = Payment_GatewaySerializer
    permission_classes = [permissions.IsAuthenticated]

class Prepared_ReportViewSet(viewsets.ModelViewSet):
    queryset = Prepared_Report.objects.all()
    serializer_class = Prepared_ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

class Report_ColumnViewSet(viewsets.ModelViewSet):
    queryset = Report_Column.objects.all()
    serializer_class = Report_ColumnSerializer
    permission_classes = [permissions.IsAuthenticated]

class Report_FilterViewSet(viewsets.ModelViewSet):
    queryset = Report_Filter.objects.all()
    serializer_class = Report_FilterSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

class Role_ProfileViewSet(viewsets.ModelViewSet):
    queryset = Role_Profile.objects.all()
    serializer_class = Role_ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class Scheduled_Job_LogViewSet(viewsets.ModelViewSet):
    queryset = Scheduled_Job_Log.objects.all()
    serializer_class = Scheduled_Job_LogSerializer
    permission_classes = [permissions.IsAuthenticated]

class Scheduled_Job_TypeViewSet(viewsets.ModelViewSet):
    queryset = Scheduled_Job_Type.objects.all()
    serializer_class = Scheduled_Job_TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class Server_ScriptViewSet(viewsets.ModelViewSet):
    queryset = Server_Script.objects.all()
    serializer_class = Server_ScriptSerializer
    permission_classes = [permissions.IsAuthenticated]

class Session_DefaultViewSet(viewsets.ModelViewSet):
    queryset = Session_Default.objects.all()
    serializer_class = Session_DefaultSerializer
    permission_classes = [permissions.IsAuthenticated]

class Sms_ParameterViewSet(viewsets.ModelViewSet):
    queryset = Sms_Parameter.objects.all()
    serializer_class = Sms_ParameterSerializer
    permission_classes = [permissions.IsAuthenticated]

class Sms_SettingsViewSet(viewsets.ModelViewSet):
    queryset = Sms_Settings.objects.all()
    serializer_class = Sms_SettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Success_ActionViewSet(viewsets.ModelViewSet):
    queryset = Success_Action.objects.all()
    serializer_class = Success_ActionSerializer
    permission_classes = [permissions.IsAuthenticated]

class System_SettingsViewSet(viewsets.ModelViewSet):
    queryset = System_Settings.objects.all()
    serializer_class = System_SettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

class Transaction_LogViewSet(viewsets.ModelViewSet):
    queryset = Transaction_Log.objects.all()
    serializer_class = Transaction_LogSerializer
    permission_classes = [permissions.IsAuthenticated]

class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDocument_TypeViewSet(viewsets.ModelViewSet):
    queryset = UserDocument_Type.objects.all()
    serializer_class = UserDocument_TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserEmailViewSet(viewsets.ModelViewSet):
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserGroup_MemberViewSet(viewsets.ModelViewSet):
    queryset = UserGroup_Member.objects.all()
    serializer_class = UserGroup_MemberSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserSelect_Document_TypeViewSet(viewsets.ModelViewSet):
    queryset = UserSelect_Document_Type.objects.all()
    serializer_class = UserSelect_Document_TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserSocial_LoginViewSet(viewsets.ModelViewSet):
    queryset = UserSocial_Login.objects.all()
    serializer_class = UserSocial_LoginSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserType_ModuleViewSet(viewsets.ModelViewSet):
    queryset = UserType_Module.objects.all()
    serializer_class = UserType_ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = [permissions.IsAuthenticated]


