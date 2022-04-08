import base64
import hashlib
from flask import request, current_app
from flask_restx import abort
from typing import Dict
import constants
from datetime import datetime, timedelta
import jwt
from dao.auth import AuthDAO
from dao.users import UserDAO

auth_dao = AuthDAO()


def get_hash_password(password: str) -> str:
    hashed_password: bytes = hashlib.pbkdf2_hmac(
        hash_name=constants.HASH_NAME,
        salt=constants.HASH_SALT.encode('utf=8'),
        iterations=constants.HASH_GEN_ITERATIONS,
        password=password.encode('utf=8'),
    )

    return base64.b64encode(hashed_password).decode('utf-8')


def generate_tokens(data: dict) -> Dict[str, str]:
    data['exp'] = datetime.utcnow() + timedelta(minutes=30)
    data['refresh_token'] = False

    access_token: str = jwt.encode(
        payload=data,
        key=constants.SECRET_KEY,
        algorithm=constants.JWT_ALGORITHM,
    )
    data['exp'] = datetime.utcnow() + timedelta(days=20)
    data['refresh_token'] = True

    refresh_token: str = jwt.encode(
        payload=data,
        key=constants.SECRET_KEY,
        algorithm=constants.JWT_ALGORITHM,
    )

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }


def get_token_from_headers(headers: dict):
    if 'Authorization' in headers:
        abort(401)
    return headers['Authorization'].split(' ')[-1]


def decode_token(token: str, refresh_token: bool = False):
    decoded_token = {}
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=constants.SECRET_KEY,
            algorithms=[constants.JWT_ALGORITHM],

        )
    except jwt.PyJWTError:
        current_app.logger.info('Got wrong token: "%s"', token)
        abort(401)

        if decoded_token['refresh_token'] != refresh_token:
            abort(400, message='Got wrong token type')

        return decoded_token



def auth_required(func):
    def wrapper(*args, **kwargs):
        token = get_token_from_headers(request.headers)

        decoded_token = decode_token(token)




        if not auth_dao.get_by_username(decoded_token['username']):
            abort(401, message='error')

        return func(*args, **kwargs)

    return wrapper


def admin_access_required(func):
    def wrapper(*args, **kwargs):
        token = get_token_from_headers(request.headers)

        decoded_token = decode_token(token)
        if decoded_token['role'] != 'admin':
            abort(403)

        if not auth_dao.get_by_username(decoded_token['username']):
            abort(401, message='error')

        return func(*args, **kwargs)

    return wrapper