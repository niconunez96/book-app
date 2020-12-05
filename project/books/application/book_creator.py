from books.domain.book_repository import BookRepository
from books.domain.author_repository import AuthorRepository
from books.domain import EntityNotFound
from books.domain.book import Book
from books.domain.author import Author


class AuthorDoesNotExist(Exception):
    pass


class BookCreator:

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

    def execute(self, author_id: int, book_body: dict) -> int:
        author = self._find_author(author_id)
        new_book = Book(book_body['title'], book_body['description'], author)
        book_saved = self.book_repository.save(new_book)
        return book_saved.id
