import json
import pickle

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def read(self):
        return f"Reading '{self.title}' by {self.author}."

    def get_info(self):
        return f"{self.title} by {self.author}, published in {self.year}."

    class BookEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Book):
                return {
                    'title': obj.title,
                    'author': obj.author,
                    'year': obj.year
                }
            return json.JSONEncoder.default(self, obj)

    def to_json(self):
        return json.dumps(self, cls=self.BookEncoder)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Book(data['title'], data['author'], data['year'])

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickle_data):
        return pickle.loads(pickle_data)

# Пример использования
book = Book("1984", "George Orwell", 1949)
json_data = book.to_json()
print(json_data)
new_book = Book.from_json(json_data)
print(new_book.read())
pickle_data = book.to_pickle()
new_book_from_pickle = Book.from_pickle(pickle_data)
print(new_book_from_pickle.get_info())