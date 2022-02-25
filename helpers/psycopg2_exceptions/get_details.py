def get_details_psycopg2_exception(exception) -> str:
    exception = exception.args[0].orig
    return exception.pgerror
