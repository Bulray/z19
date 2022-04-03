from application.dao.users import UserDAO
from application.dao.auth import AuthDAO
from application.services.users import UsersService
from application.services.auth import AuthService

user_service = UsersService(dao=UserDAO())
auth_service = AuthService(dao=AuthDAO())