from dao.model.user_model import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        return self.session.query(User).all()

    def get_one_user(self, uid):
        return self.session.query(User).get(uid)

    def add_user(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user):
        self.session.add(user)
        self.session.commit()
        return user
