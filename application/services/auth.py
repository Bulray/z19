from flask_restx import abort
from application.dao.auth import AuthDAO
from application.utils import get_hash_passwoerd, generate_tokens


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def login(self, data: dict):
        user_data = self.dao.get_by_username((data['username']))
        if user_data is None:
            abort(401, message='user not found')

        hash_password = get_hash_passwoerd(data['password'])
        if user_data['password'] != hash_password:
            abort(401, message='invalid parameters')

        tokens: dict = generate_tokens(
            {
                'username': data['username'],
                'role': user_data['role'],
             },
        )
        return tokens

    def get_new_tokens(self, refresh_token, str):
        decoded_token = decode_token(refresh_token, refresh_token=True)

        tokens = generate_tokens(
            data={
                'username': decoded_token['username'],
                'role': decoded_token['role']
            },
        )
        return tokens


