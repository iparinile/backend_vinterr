import datetime

import jwt

from helpers.auth.exception import ReadTokenException

secret_key_user = 'hgxox4sJPEIKBJKGgBfuqR9HU6792wwFlW/KVCw2m68='
secret_key_customer = 'PSnhXNuT6fRu1/Le7NLbfUILkC2iCBrgeBlJmmIuJfM='


def create_token(payload: dict) -> str:
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    if payload['role'] == "admin":
        return jwt.encode(payload, secret_key_user, algorithm='HS256')
    else:
        return jwt.encode(payload, secret_key_customer, algorithm='HS256')


def read_token(token: str, role: str) -> dict:
    if role == "admin":
        secret_key = secret_key_user
    else:
        secret_key = secret_key_customer
    try:
        return jwt.decode(token, secret_key, algorithms='HS256')
    except jwt.exceptions.PyJWTError:
        raise ReadTokenException
