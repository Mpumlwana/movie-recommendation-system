class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.watchlist = []  # New property for Issue #18

    def login(self):
        return f"{self.name} logged in"

    def rate_movie(self, movie, rating):
        return f"{self.name} rated {movie.title} with {rating}"

    def get_recommendations(self):
        return "Fetching recommendations"

    # --- New Methods for Watchlist ---
    def add_to_watchlist(self, movie_id: str):
        if movie_id not in self.watchlist:
            self.watchlist.append(movie_id)
        return self.watchlist

    def remove_from_watchlist(self, movie_id: str):
        if movie_id in self.watchlist:
            self.watchlist.remove(movie_id)
        return self.watchlist