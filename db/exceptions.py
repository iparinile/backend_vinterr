class DBIntegrityException(Exception):
    pass


class DBDataException(Exception):
    pass


'''
Users Exceptions
'''


class DBUserExistsException(Exception):
    pass


class DBUserNotExistsException(Exception):
    pass


'''
Customers Exceptions
'''


class DBCustomerLoginExistsException(Exception):
    pass


class DBCustomerEmailExistsException(Exception):
    pass


class DBCustomerPhoneNumberExistsException(Exception):
    pass


class DBCustomerNotExistsException(Exception):
    pass


'''
Materials Exceptions
'''


class DBMaterialExistsException(Exception):
    pass


class DBMaterialNotExistsException(Exception):
    pass


'''
Categories Exceptions
'''


class DBCategoryExistsException(Exception):
    pass


class DBCategoryNotExistsException(Exception):
    pass


'''
Structures Exceptions
'''


class DBStructureExistsException(Exception):
    pass


class DBStructureNotExistsException(Exception):
    pass


'''
ProductsCare Exceptions
'''


class DBProductsCareExistsException(Exception):
    pass


class DBProductsCareNotExistsException(Exception):
    pass


'''
Sizes Exceptions
'''


class DBSizeExistsException(Exception):
    pass


class DBSizeNotExistsException(Exception):
    pass


'''
Colors Exceptions
'''


class DBColorNameExistsException(Exception):
    pass


class DBColorNotExistsException(Exception):
    pass


'''
Goods Exceptions
'''


class DBGoodNotExistsException(Exception):
    pass


class DBVariationsForGoodNotExistsException(Exception):
    pass


'''
Variations Exceptions
'''


class DBVariationNotExistsException(Exception):
    pass


class DBVariationNegativeRest(Exception):
    pass


'''
DeliveryTypes Exceptions
'''


class DBDeliveryTypeNotExistsException(Exception):
    pass


class DBDeliveryTypeExistsException(Exception):
    pass


'''
Orders Exceptions
'''


class DBOrderNotExistsException(Exception):
    pass


class DBOrderExistsException(Exception):
    pass


'''
TelegramUsers Exceptions
'''


class DBTelegramUserExistsException(Exception):
    pass


class DBTelegramUserNotExistsException(Exception):
    pass


'''
Statuses Exceptions
'''


class DBStatusExistsException(Exception):
    pass


class DBStatusNotExistsException(Exception):
    pass


'''
Images Exceptions
'''


class DBImageNotExistsException(Exception):
    pass
