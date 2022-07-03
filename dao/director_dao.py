from dao.model.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_one_director(self, did):
        return self.session.query(Director).get(did)

    def add_director(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update_director(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete_director(self, did):
        director = self.get_one_director(did)
        self.session.delete(director)
        self.session.commit()


