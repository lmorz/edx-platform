from import_shims.warn import warn_deprecated_import

warn_deprecated_import('track.management', 'common.djangoapps.track.management')

from common.djangoapps.track.management import *
