from typing import List

from books.domain.book_repository import BookRepository


class BooksFinder:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self) -> List[dict]:
        books = self.book_repository.find_all()
        return [book.to_dict() for book in books]


class BookFinder:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: int) -> dict:
        return self.book_repository.find_by_id(book_id).to_dict()
