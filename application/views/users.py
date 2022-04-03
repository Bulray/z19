from flask import request
from flask_restx import Namespace, Resource
from application.container import user_service

users_ns = Namespace('users')

@users_ns.route('/')
class UsersView(Resource):
    def post(self):
      user_service.register(request.json)
      return {}, 201


