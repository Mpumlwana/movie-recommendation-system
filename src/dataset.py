class Dataset:
    def __init__(self, dataset_id, source):
        self.dataset_id = dataset_id
        self.source = source

    def upload_dataset(self):
        return "Dataset uploaded"

    def validate_dataset(self):
        return True