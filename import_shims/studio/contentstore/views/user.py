from import_shims.warn import warn_deprecated_import

warn_deprecated_import('contentstore.views.user', 'cms.djangoapps.contentstore.views.user')

from cms.djangoapps.contentstore.views.user import *
