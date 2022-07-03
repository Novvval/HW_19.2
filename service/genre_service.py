from dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all_genres(self):
        return self.genre_dao.get_all_genres()

    def get_one_genre(self, gid):
        return self.genre_dao.get_one_genre(gid)

    def add_genre(self, data):
        return self.genre_dao.add_genre(data)

    def update_genre(self, data):
        gid = data["id"]
        genre = self.genre_dao.add_genre(gid)
        genre.name = data["name"]
        return self.genre_dao.update_genre(genre)

    def delete_genre(self, gid):
        return self.genre_dao.delete_genre(gid)
