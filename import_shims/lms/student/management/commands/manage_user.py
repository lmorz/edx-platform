from import_shims.warn import warn_deprecated_import

warn_deprecated_import('student.management.commands.manage_user', 'common.djangoapps.student.management.commands.manage_user')

from common.djangoapps.student.management.commands.manage_user import *
