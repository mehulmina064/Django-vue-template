from rest_framework import serializers


#models

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
class Access_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_Log
        fields = '__all__'

#create serializer for activity_log
class Activity_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_Log
        fields = '__all__'

#create serializer for doctype
class DoctypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctype
        fields = '__all__'

#create serializer for block_module
class Block_ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block_Module
        fields = '__all__'

#create serializer for comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

#create serializer for communication
class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'
    
#create serializer for communication_link  
class Communication_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication_Link
        fields = '__all__'

#create serializer for communication_docperm
class Communication_DocpermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication_Docperm
        fields = '__all__'

#create serializer for data_import
class Data_ImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_Import
        fields = '__all__'

#create serializer for data_export
class Data_ExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_Export
        fields = '__all__'

#create serializer for data_import_log
class Data_Import_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_Import_Log
        fields = '__all__'

#create serializer for defaultvalue
class DefaultValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultValue
        fields = '__all__'

#create serializer for deleted_document
class Deleted_DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deleted_Document
        fields = '__all__'

#create serializer for docfield
class DocfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docfield
        fields = '__all__'

#create serializer for docshare
class DocshareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docshare
        fields = '__all__'

#create serializer for doctype_action
class Doctype_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctype_Action
        fields = '__all__'

#create serializer for doctype_link
class Doctype_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctype_Link
        fields = '__all__'

#create serializer for doctype_state
class Doctype_StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctype_State
        fields = '__all__'

#create serializer for domain
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'

#create serializer for domain_settings
class Domain_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain_Settings
        fields = '__all__'

#create serializer for Dynamic_Link
class Dynamic_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dynamic_Link
        fields = '__all__'

#create serializer for error_log
class Error_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error_Log
        fields = '__all__'

#create serializer for error_snapshot
class Error_SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error_Snapshot
        fields = '__all__'

#create serializer for feedback
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

#create serializer for file
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

#create serializer for has_domain
class Has_DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Has_Domain
        fields = '__all__'

#create serializer for has_role
class Has_RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Has_Role
        fields = '__all__'

#create serializer for install_application
class Install_ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Install_Application
        fields = '__all__'

#create serializer for language
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

#create serializer for log_setting_user
class Log_Setting_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Setting_User
        fields = '__all__'

#create serializer for log_settings
class Log_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Settings
        fields = '__all__'

#create serializer for module_def
class Module_DefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module_Def
        fields = '__all__'

#create serializer for module_profile
class Module_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module_Profile
        fields = '__all__'

#create serializer for navbar_item
class Navbar_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar_Item
        fields = '__all__'

#create serializer for navbar_settings
class Navbar_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar_Settings
        fields = '__all__'

#create serializer for package
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

#create serializer for page
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

#create serializer for Payment_Gateway
class Payment_GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Gateway
        fields = '__all__'

#create serializer for Prepared_Report
class Prepared_ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prepared_Report
        fields = '__all__'

#create serializer for report_column
class Report_ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report_Column
        fields = '__all__'

#create serializer for report_filter
class Report_FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report_Filter
        fields = '__all__'

#create serializer for report
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

#create serializer for role_profile
class Role_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Profile
        fields = '__all__'

#create serializer for scheduled_job_log
class Scheduled_Job_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduled_Job_Log
        fields = '__all__'

#create serializer for scheduled_job_type
class Scheduled_Job_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduled_Job_Type
        fields = '__all__'

#create serializer for server_script
class Server_ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server_Script
        fields = '__all__'


#create serializer for session_default
class Session_DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session_Default
        fields = '__all__'

#create serializer for sms_parameter
class Sms_ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms_Parameter
        fields = '__all__'

#create serializer for sms_settings
class Sms_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms_Settings
        fields = '__all__'

#create serializer for success_action
class Success_ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Success_Action
        fields = '__all__'

#create serializer for System_Settings
class System_SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_Settings
        fields = '__all__'

#create serializer for test
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

#create serializer for transaction_log
class Transaction_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_Log
        fields = '__all__'


#create serializer for translation
class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'

#create serializer for userDocument_type
class UserDocument_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocument_Type
        fields = '__all__'

#create serializer for user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


#create serializer for UserEmail,UserGroup,UserGroup_Member,UserSelect_Document_Type,UserSocial_Login,UserType_Module
class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmail
        fields = '__all__'

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'

class UserGroup_MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup_Member
        fields = '__all__'

class UserSelect_Document_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSelect_Document_Type
        fields = '__all__'

class UserSocial_LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocial_Login
        fields = '__all__'

class UserType_ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType_Module
        fields = '__all__'

#create serializer for usertype
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'

#create serializer for version
class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

#create serializer for role
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

        
