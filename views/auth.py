from flask import request
from flask_restx import Namespace, Resource
from container import auth_service

auth_ns = Namespace('auth')

@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        return auth_service.login(request.json)

    def put(self):
        return auth_service.get_new_tokens(request.json['refresh_token'])

