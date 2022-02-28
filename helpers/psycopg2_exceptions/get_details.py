def get_details_psycopg2_exception(exception) -> tuple:
    exception = exception.args[0].orig
    exception_code = exception.pgcode
    exception_info = exception.pgerror
    return exception_code, exception_info
