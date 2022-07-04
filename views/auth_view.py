from flask import request
from flask_restx import Namespace, Resource
from implemented import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        data = request.get_json()
        return auth_service.create_tokens(data)

    def put(self):
        data = request.get_json()
        return auth_service.update(data)

