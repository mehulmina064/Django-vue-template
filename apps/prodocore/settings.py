from django.conf import settings
from django.utils.text import slugify

COR_SETTINGS = getattr(settings, 'COR', {})

SETTINGS_PERMISSIONS = COR_SETTINGS.get('PERMISSIONS', {})
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
    'AUTH_MODELS_SYNC': COR_SETTINGS.get('AUTH_MODELS_SYNC', False),
    'AUTH_MODELS_GET_OR_CREATE': COR_SETTINGS.get('AUTH_MODELS_GET_OR_CREATE', True),
    'GROUP_NAME_PREFIX': COR_SETTINGS.get('GROUP_NAME_PREFIX', 'DGM_'),
    'GROUP_NAME_SUFFIX': COR_SETTINGS.get('GROUP_NAME_SUFFIX', '_$$random'),
    'USER_USERNAME_PREFIX': COR_SETTINGS.get('USER_USERNAME_PREFIX', 'DGM_'),
    'USER_USERNAME_SUFFIX': COR_SETTINGS.get('USER_USERNAME_SUFFIX', '_$$random'),
    # Permissions
    'PERMISSIONS': PERMISSIONS,
    # Templates
    'TEMPLATE_STYLE': COR_SETTINGS.get('TEMPLATE_STYLE', 'bootstrap3'),
    # Slugify function
    'SLUGIFY_FUNCTION':  COR_SETTINGS.get('SLUGIFY_FUNCTION', slugify_function),
    'SLUGIFY_USERNAME_FUNCTION':  COR_SETTINGS.get('SLUGIFY_USERNAME_FUNCTION', slugify_username_function),
}
