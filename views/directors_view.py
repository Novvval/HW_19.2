from flask import request
from flask_restx import Resource, Namespace
from sqlalchemy.exc import NoResultFound
from dao.model.director_model import directors_schema, director_schema
from implemented import director_service
from views.decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all_directors()

        return directors_schema.dump(directors), 200

    @admin_required
    def post(self):
        data = request.get_json()
        director_service.add_director(data)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        try:
            director = director_service.get_one_director(did)
        except NoResultFound as e:
            return f"{e}", 400

        return director_schema.dump(director), 200

    @admin_required
    def put(self, did):
        data = request.get_json()
        data["id"] = did
        director_service.update_director(data)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete_director(did)
        return "", 204
