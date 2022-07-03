from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from views.decorators import auth_required, admin_required
from dao.model.movie_model import movies_schema, movie_schema

movie_ns = Namespace("movies")


@movie_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)

        if director_id:
            movies = movie_service.get_movies_by_director(director_id)
        elif genre_id:
            movies = movie_service.get_movies_by_genre(genre_id)
        elif year:
            movies = movie_service.get_movies_by_year(year)
        else:
            movies = movie_service.get_all_movies()

        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        data = request.get_json()
        movie_service.add_movie(data)
        return "", 201


@movie_ns.route('/<int:mid>')
class GenreView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one_movie(mid)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid):
        data = request.get_json()
        data["id"] = mid

        movie_service.update_movie(data)
        return "", 204

    @admin_required
    def patch(self, mid):
        data = request.get_json()
        data["id"] = mid

        movie_service.update_movie_partial(data)
        return "", 204

    @admin_required
    def delete(self, mid):
        movie_service.delete_movie(mid)
        return "", 204
