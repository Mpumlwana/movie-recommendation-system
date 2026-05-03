class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def login(self):
        return f"{self.name} logged in"

    def rate_movie(self, movie, rating):
        return f"{self.name} rated {movie.title} with {rating}"

    def get_recommendations(self):
        return "Fetching recommendations"