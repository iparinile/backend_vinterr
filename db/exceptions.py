class DBIntegrityException(Exception):
    pass


class DBDataException(Exception):
    pass


class DBUserExistsException(Exception):
    pass


class DBUserNotExistsException(Exception):
    pass


class DBCustomerLoginExistsException(Exception):
    pass


class DBCustomerEmailExistsException(Exception):
    pass


class DBCustomerPhoneNumberExistsException(Exception):
    pass


class DBCustomerNotExistsException(Exception):
    pass


class DBMaterialExistsException(Exception):
    pass


class DBMaterialNotExistsException(Exception):
    pass


class DBCategoryExistsException(Exception):
    pass


class DBCategoryNotExistsException(Exception):
    pass


class DBStructureExistsException(Exception):
    pass


class DBStructureNotExistsException(Exception):
    pass


class DBSizeExistsException(Exception):
    pass


class DBSizeNotExistsException(Exception):
    pass
