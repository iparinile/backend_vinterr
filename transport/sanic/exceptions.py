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
