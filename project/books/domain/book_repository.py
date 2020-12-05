from typing import List
from books.domain.book import Book


class BookRepository:

    def find_all(self) -> List[Book]:
        raise NotImplementedError

    def find_by_id(self, id: int) -> Book:
        raise NotImplementedError

    def find_by_author(self, author_id: int) -> List[Book]:
        raise NotImplementedError

    def save(self, entity: Book) -> Book:
        raise NotImplementedError
