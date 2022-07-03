from flask import request
from flask_restx import Resource, Namespace
from dao.model.user_model import user_schema, users_schema
from implemented import user_service

user_ns = Namespace("users")


@user_ns.route("/")
class UsersView(Resource):
    def get(self):
        users = user_service.get_all_users()
        return users_schema.dump(users), 200

    def post(self):
        data = request.get_json()
        user_service.add_user(data)
        return "", 201


@user_ns.route("<int:uid>")
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one_user(uid)
        return user_schema.dump(user), 200

    def put(self, uid):
        data = request.get_json()
        data["id"] = uid
        user_service.update_user(data)
        return "", 204
