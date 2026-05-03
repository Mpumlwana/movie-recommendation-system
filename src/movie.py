class Movie:
    def __init__(self, movie_id, title, genre):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre

    def get_details(self):
        return f"{self.title} - {self.genre}"

    def update_movie(self, title):
        self.title = title