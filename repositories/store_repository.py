from models.store import Store

class StoreRepository:
    def __init__(self):
        self.stores = [
            Store(id=1, name='Tienda de Juan', user_id=1),
            Store(id=2, name='Tienda de Laura', user_id=2)
        ]

    def find_by_user(self, user_id):
        return [store for store in self.stores if store.user_id == user_id]
