from flask import Flask
from flask_restx import Api
from lesson19_project_easy_source.views.auth import auth_ns
from lesson19_project_easy_source.views.users import users_ns
from lesson19_project_easy_source.views.protected import protected_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    api = Api(app, prefix='/api')
    api.add_namespace(auth_ns)
    api.add_namespace(users_ns)
    api.add_namespace(protected_ns)

    return app