class Search:
    def __init__(self, query):
        self.query = query

    def search_movies(self):
        return f"Searching for {self.query}"