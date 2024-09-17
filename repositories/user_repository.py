from models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User(id=1, name='Juan Pérez'),
            User(id=2, name='Laura García')
        ]

    def get_all(self):
        return self.users

    def delete(self, user_id):
        self.users = [user for user in self.users if user.id != user_id]
