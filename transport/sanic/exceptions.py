from sanic.exceptions import SanicException


class SanicRequestValidationException(SanicException):
    status_code = 400


class SanicAuthException(SanicException):
    status_code = 401


class SanicResponseValidationException(SanicException):
    status_code = 500


class SanicPasswordHashException(SanicException):
    status_code = 500


class SanicDBException(SanicException):
    status_code = 500


class SanicLogsException(SanicException):
    status_code = 500


class SanicDBUniqueFieldException(SanicException):
    status_code = 409


class SanicRegisterPaymentException(SanicException):
    status_code = 409


class SanicInvalidRequestParameterException(SanicException):
    status_code = 400


'''
Users Exceptions
'''


class SanicUserConflictException(SanicException):
    status_code = 409


class SanicUserNotFound(SanicException):
    status_code = 404


'''
Customers Exceptions
'''


class SanicCustomerConflictException(SanicException):
    status_code = 409


class SanicCustomerNotFound(SanicException):
    status_code = 404


'''
Materials Exceptions
'''


class SanicMaterialConflictException(SanicException):
    status_code = 409


class SanicMaterialNotFound(SanicException):
    status_code = 404


'''
Categories Exceptions
'''


class SanicCategoryConflictException(SanicException):
    status_code = 409


class SanicCategoryNotFound(SanicException):
    status_code = 404


'''
Structures Exceptions
'''


class SanicStructureConflictException(SanicException):
    status_code = 409


class SanicStructureNotFound(SanicException):
    status_code = 404


'''
ProductsCare Exceptions
'''


class SanicProductsCareConflictException(SanicException):
    status_code = 409


class SanicProductsCareNotFound(SanicException):
    status_code = 404


'''
Sizes Exceptions
'''


class SanicSizeConflictException(SanicException):
    status_code = 409


class SanicSizeNotFound(SanicException):
    status_code = 404


'''
Colors Exceptions
'''


class SanicColorConflictException(SanicException):
    status_code = 409


class SanicColorNotFound(SanicException):
    status_code = 404


'''
Goods Exceptions
'''


class SanicGoodNotFound(SanicException):
    status_code = 404


class SanicVariationsForGoodNotFound(SanicException):
    status_code = 404


'''
Variations Exceptions
'''


class SanicVariationNotFound(SanicException):
    status_code = 404


class SanicInsufficientAmountVariation(SanicException):
    status_code = 400


'''
Delivery_types Exceptions
'''


class SanicDeliveryTypeConflictException(SanicException):
    status_code = 409


class SanicDeliveryTypeNotFound(SanicException):
    status_code = 404


'''
Orders Exceptions
'''


class SanicOrderNotFound(SanicException):
    status_code = 404


class SanicSberbankIdConflictException(SanicException):
    status_code = 409


class SanicNoVariationsInOrder(SanicException):
    status_code = 400


'''
Statuses Exceptions
'''


class SanicStatusConflictException(SanicException):
    status_code = 409


class SanicStatusNotFound(SanicException):
    status_code = 404


'''
TelegramUsers Exceptions
'''


class SanicTelegramUserConflictException(SanicException):
    status_code = 409


class SanicTelegramUserNotFound(SanicException):
    status_code = 404


'''
Images Exceptions
'''


class SanicIncorrectRequest(SanicException):
    status_code = 400


class SanicWrongImagePath(SanicException):
    status_code = 400
