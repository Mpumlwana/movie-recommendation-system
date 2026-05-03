class MovieFactory:
    @staticmethod
    def create_movie(movie_type):
        if movie_type == "action":
            return "Action Movie Created"
        elif movie_type == "comedy":
            return "Comedy Movie Created"
        else:
            return "Unknown Movie Type"