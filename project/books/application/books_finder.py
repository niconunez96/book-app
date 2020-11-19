from typing import List

from project.books.domain.book import Book
from project.books.domain.book_repository import BookRepository


class BooksFinder:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self) -> List[Book]:
        return self.book_repository.find_all()
