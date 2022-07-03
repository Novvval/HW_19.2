from flask import request
from flask_restx import Resource, Namespace
from implemented import genre_service
from views.decorators import auth_required, admin_required
from dao.model.genre_model import genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all_genres()
        return genres_schema.dump(genres), 200

    @admin_required
    def post(self):
        data = request.get_json()
        genre_service.add_genre(data)
        return "", 204


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one_genre(gid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid):
        data = request.get_json()
        data["id"] = gid
        genre_service.update_genre(data)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete_genre(gid)
        return "", 204
