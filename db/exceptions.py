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


class DBColorCodeExistsException(Exception):
    pass


class DBColorNotExistsException(Exception):
    pass


'''
Goods Exceptions
'''


class DBGoodNotExistsException(Exception):
    pass
