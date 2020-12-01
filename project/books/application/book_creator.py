from books.domain.book_repository import BookRepository
from books.domain.book import Book


class BookCreator:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_body: dict) -> int:
        new_book = Book(book_body['title'], book_body['description'])
        self.book_repository.save(new_book)
