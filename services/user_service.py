from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_all()

    def delete_user(self, user_id):
        self.user_repository.delete(user_id)
