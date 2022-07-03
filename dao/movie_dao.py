from dao.model.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_one_movie(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movies_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_movies_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_movies_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def add_movie(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete_movie(self, mid):
        book = self.get_one_movie(mid)
        self.session.delete(book)
        self.session.commit()
