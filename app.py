from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.auth_view import auth_ns
from views.movies_view import movie_ns
from views.genres_view import genre_ns
from views.user_view import user_ns


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


config = Config()
app = create_app(config)
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
