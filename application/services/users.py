from application.dao.users import UserDAO
from application.utils import get_hash_passwoerd

class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register(self, data: dict) -> dict:
        data['password'] = get_hash_passwoerd(data['password'])
        self.dao.create(data)
        return data
