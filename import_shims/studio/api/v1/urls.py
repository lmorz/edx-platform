from import_shims.warn import warn_deprecated_import

warn_deprecated_import('api.v1.urls', 'cms.djangoapps.api.v1.urls')

from cms.djangoapps.api.v1.urls import *
