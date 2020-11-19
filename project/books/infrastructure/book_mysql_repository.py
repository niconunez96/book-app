from datetime import datetime
from typing import List

from project.books.domain.book_repository import BookRepository
from project.books.domain.book import Book


class BookMySQLRepository(BookRepository):

    def find_all(self) -> List[Book]:
        return [
            Book("New book", "Some description", datetime.now()),
            Book("New book 2", "Some description 2", datetime.now()),
        ]

    def find_by_id(self, id: int) -> Book:
        Book("New book", "Some description", datetime.now()),

    def save(self, entity: Book) -> Book:
        Book("New book", "Some description", datetime.now()),
