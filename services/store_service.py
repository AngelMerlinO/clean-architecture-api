from repositories.store_repository import StoreRepository

class StoreService:
    def __init__(self):
        self.store_repository = StoreRepository()

    def get_stores_by_user(self, user_id):
        return self.store_repository.find_by_user(user_id)
