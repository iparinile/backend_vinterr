from sanic.exceptions import SanicException


class SanicRequestValidationException(SanicException):
    status_code = 400


class SanicUserConflictException(SanicException):
    status_code = 409


class SanicCustomerConflictException(SanicException):
    status_code = 409


class SanicCustomerNotFound(SanicException):
    status_code = 404


class SanicResponseValidationException(SanicException):
    status_code = 500


class SanicPasswordHashException(SanicException):
    status_code = 500


class SanicDBException(SanicException):
    status_code = 500


class SanicUserNotFound(SanicException):
    status_code = 404


class SanicAuthException(SanicException):
    status_code = 401


class SanicLogsException(SanicException):
    status_code = 500


class SanicMaterialConflictException(SanicException):
    status_code = 409


class SanicMaterialNotFound(SanicException):
    status_code = 404


class SanicCategoryConflictException(SanicException):
    status_code = 409


class SanicCategoryNotFound(SanicException):
    status_code = 404


class SanicStructureConflictException(SanicException):
    status_code = 409


class SanicStructureNotFound(SanicException):
    status_code = 404


class SanicSizeConflictException(SanicException):
    status_code = 409


class SanicSizeNotFound(SanicException):
    status_code = 404
