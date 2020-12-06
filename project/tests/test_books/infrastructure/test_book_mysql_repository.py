import pytest

from books.infrastructure.book_mysql_repository import BookMySQLRepository
from books.domain import EntityNotFound
from tests.test_books.factory.book_factory import BookFactory
from tests.test_books.factory.author_factory import AuthorFactory


class TestBookMySQLRepository:

    def test_should_return_book_with_id_specified(self, db_test):
        book = BookFactory.create(id=1)
        book_repository = BookMySQLRepository()

        book_found = book_repository.find_by_id(1)
        assert book_found.to_dict() == book.to_dict()

    def test_should_raise_entity_not_found_when_id_does_not_exist(
        self,
        db_test,
    ):
        book_repository = BookMySQLRepository()
        with pytest.raises(EntityNotFound):
            book_repository.find_by_id(-1)

    def test_should_return_all_books_stored(self, db_test):
        BookFactory.create_batch(size=5)
        book_repository = BookMySQLRepository()

        books_found = book_repository.find_all()

        assert len(books_found) == 5

    def test_should_return_books_related_with_an_author(
        self,
        db_test,
    ):
        author = AuthorFactory.create()
        BookFactory.create_batch(size=3, author=author, author_id=author.id)
        BookFactory.create_batch(size=10)
        book_repository = BookMySQLRepository()

        books_found = book_repository.find_by_author(1)
        assert len(books_found) == 3

    def test_should_save_book_with_id(self, db_test):
        book_repository = BookMySQLRepository()

        book = BookFactory.build(title="My awesome book")
        assert book.id is None

        book_saved = book_repository.save(book)

        assert book_saved.id
        assert book_saved.title == "My awesome book"
