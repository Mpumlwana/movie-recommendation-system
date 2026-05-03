class RecommendationBuilder:
    def __init__(self):
        self.steps = []

    def add_data(self):
        self.steps.append("Data added")
        return self

    def build_model(self):
        self.steps.append("Model built")
        return self

    def get_result(self):
        return self.steps