import json
from library_manager.book import Book

class LibraryInventory:
    def _init_(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)
                for item in data:
                    book = Book(
                        item["title"],
                        item["author"],
                        item["isbn"],
                        item["status"]
                    )
                    self.books.append(book)
        except:
            self.books = []

    def save_books(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books available")
        for book in self.books:
            print(book)