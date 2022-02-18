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
