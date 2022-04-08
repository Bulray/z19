from dao.users import UserDAO
from dao.auth import AuthDAO
from services.users import UsersService
from services.auth import AuthService

user_service = UsersService(dao=UserDAO)
auth_service = AuthService(dao=AuthDAO)
