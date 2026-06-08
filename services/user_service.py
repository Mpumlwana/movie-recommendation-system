from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def get_watchlist(self, user_id: str):
        user = self.repo.find_by_id(user_id)
        if not user:
            raise Exception("User not found")
        return user.watchlist

    def add_to_watchlist(self, user_id: str, movie_id: str):
        user = self.repo.find_by_id(user_id)
        if not user:
            raise Exception("User not found")
        
        user.add_to_watchlist(movie_id)
        self.repo.save(user)
        return user.watchlist

    def remove_from_watchlist(self, user_id: str, movie_id: str):
        user = self.repo.find_by_id(user_id)
        if not user:
            raise Exception("User not found")
        
        user.remove_from_watchlist(movie_id)
        self.repo.save(user)
        return user.watchlist