from dao.user_dao import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_one_user(self, uid):
        return self.user_dao.get_one_user(uid)

    def add_user(self, data):
        return self.user_dao.add_user(data)

    def update_user(self, data):
        uid = data["id"]
        user = self.get_one_user(uid)

        user.username = data["username"]
        user.password = data["password"]
        user.role = data["role"]
