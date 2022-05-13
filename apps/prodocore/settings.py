from django.conf import settings
from django.utils.text import slugify

PRODOCORE_SETTINGS = getattr(settings, 'PRODOCORE', {})

SETTINGS_PERMISSIONS = PRODOCORE_SETTINGS.get('PERMISSIONS', {})
PERMISSIONS = {
    'owner': ['view', 'change', 'delete'],
    'group': ['view', 'change'],
    'groups_upstream': ['view'],
    'groups_downstream': [],
    'groups_siblings': ['view'],
}
PERMISSIONS.update(SETTINGS_PERMISSIONS)

def slugify_function(s):
    return slugify(s).lower()

def slugify_username_function(s):
    return slugify_function(s).replace('-', '_')


GROUPS_MANAGER = {
    # User and Groups sync settings
    'AUTH_MODELS_SYNC': PRODOCORE_SETTINGS.get('AUTH_MODELS_SYNC', False),
    'AUTH_MODELS_GET_OR_CREATE': PRODOCORE_SETTINGS.get('AUTH_MODELS_GET_OR_CREATE', True),
    'GROUP_NAME_PREFIX': PRODOCORE_SETTINGS.get('GROUP_NAME_PREFIX', 'DGM_'),
    'GROUP_NAME_SUFFIX': PRODOCORE_SETTINGS.get('GROUP_NAME_SUFFIX', '_$$random'),
    'USER_USERNAME_PREFIX': PRODOCORE_SETTINGS.get('USER_USERNAME_PREFIX', 'DGM_'),
    'USER_USERNAME_SUFFIX': PRODOCORE_SETTINGS.get('USER_USERNAME_SUFFIX', '_$$random'),
    # Permissions
    'PERMISSIONS': PERMISSIONS,
    # Templates
    'TEMPLATE_STYLE': PRODOCORE_SETTINGS.get('TEMPLATE_STYLE', 'bootstrap3'),
    # Slugify function
    'SLUGIFY_FUNCTION':  PRODOCORE_SETTINGS.get('SLUGIFY_FUNCTION', slugify_function),
    'SLUGIFY_USERNAME_FUNCTION':  PRODOCORE_SETTINGS.get('SLUGIFY_USERNAME_FUNCTION', slugify_username_function),
}
