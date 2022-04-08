from dao.users import UserDAO
from utils import get_hash_password

class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register(self, data: dict) -> dict:
        data['password'] = get_hash_password(data['password'])
        self.dao.create(data)
        return data
