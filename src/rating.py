class Rating:
    def __init__(self, rating_id, score):
        self.rating_id = rating_id
        self.score = score

    def submit_rating(self):
        return "Rating submitted"

    def validate_rating(self):
        return 0 <= self.score <= 5