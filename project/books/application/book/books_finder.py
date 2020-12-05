from typing import List

from books.application.author import AuthorDoesNotExist
from books.domain import EntityNotFound
from books.domain.author import Author
from books.domain.book_repository import BookRepository
from books.domain.author_repository import AuthorRepository


class AuthorBooksFinder:
    def __init__(
        self,
        author_repository: AuthorRepository,
        book_repository: BookRepository,
    ):
        self.author_repository = author_repository
        self.book_repository = book_repository

    def _find_author(self, author_id: int) -> Author:
        try:
            return self.author_repository.find_by_id(author_id)
        except EntityNotFound:
            raise AuthorDoesNotExist

    def execute(self, author_id: int) -> List[dict]:
        author = self._find_author(author_id)
        books = self.book_repository.find_by_author(author.id)
        return [book.to_dict() for book in books]


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
