from dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all_directors(self):
        return self.director_dao.get_all_directors()

    def get_one_director(self, did):
        return self.director_dao.get_one_director(did)

    def add_director(self, data):
        return self.director_dao.add_director(data)

    def update_director(self, data):
        did = data["id"]
        director = self.get_one_director(did)
        director.name = data["name"]
        return self.director_dao.update_director(director)

    def delete_director(self, did):
        return self.director_dao.delete_director(did)