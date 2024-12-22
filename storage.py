import pickle

class FileStorage():
    '''Class for file storage handler based on pickle'''
    def __init__(self, storage_object, filename: str = "addressbook.pkl"):
        self.filename = filename
        self.storage_object = storage_object

    def save_data(self, book):
        '''Save object to file'''
        with open(self.filename, "wb") as fh:
            pickle.dump(book, fh)

    def load_data(self):
        '''Read object from file and deserialize'''
        try:
            with open(self.filename, "rb") as fh:
                return pickle.load(fh)
        except FileNotFoundError:
            return self.storage_object()