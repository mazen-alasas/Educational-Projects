import numpy as np


class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = True

    def get_book_id(self):
        return self._book_id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def is_available(self):
        return self._available

    def set_book_id(self, book_id):
        self._book_id = book_id

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_available(self, available):
        self._available = available


class Library:
    def __init__(self):
        self.books = np.array([])

    def add_book(self, book):
        self.books = np.append(self.books, book)

    def remove_book(self, book_id):
        idx = np.where(self.books.get_book_id() == book_id)[0]
        if idx.size == 0:
            print("Book ID not found.")
        else:
            self.books = np.delete(self.books, idx)

    def borrow_book(self, book_id):
        idx = np.where(self.books.get_book_id() == book_id)[0]
        if idx.size == 0:
            print("Book ID not found.")
        else:
            if self.books[idx].is_available():
                self.books[idx].set_available(False)
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")

    def return_book(self, book_id):
        idx = np.where(self.books.get_book_id() == book_id)[0]
        if idx.size == 0:
            print("Book ID not found.")
        else:
            if not self.books[idx].is_available():
                self.books[idx].set_available(True)
                print("Book returned successfully.")
            else:
                print("Book is already available.")

    def display_books(self):
        if self.books.size == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"Book ID: {book.get_book_id()}, Title: {book.get_title()}, Author: {book.get_author()}, Available: {book.is_available()}")


library = Library()

cp3 = Book(1, "cp3", "Steven Halim")
cp_handbook = Book(2, "handbook for competitive programmers", "Antti Laaksonen")
cp_guide = Book(3, "Guide to Competitive Programming", "Antti Laaksonen")

library.add_book(cp3)
library.add_book(cp_handbook)
library.display_books()
library.borrow_book(2)
library.add_book(cp_guide)
library.return_book(2)
library.remove_book(3)