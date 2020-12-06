import pytest
from tests.test_books.factory.author_factory import AuthorFactory

from books.infrastructure.author_mysql_repository import AuthorMySQLRepository
from books.domain import EntityNotFound


class TestAuthorMySQLRepository:

    def test_should_return_author_with_id_specified(self, db_test):
        author_repository = AuthorMySQLRepository()
        author = AuthorFactory.create(id=1)

        author_found = author_repository.find_by_id(1)

        assert author_found.to_dict() == author.to_dict()

    def test_should_raise_entity_not_found_when_id_does_not_exist(
        self,
        app_test,
        db_test,
    ):
        author_repository = AuthorMySQLRepository()

        with pytest.raises(EntityNotFound):
            author_repository.find_by_id(-1)

    def test_should_return_all_authors_saved(self, db_test):
        author_repository = AuthorMySQLRepository()
        AuthorFactory.create_batch(size=20)

        authors_found = author_repository.find_all()

        assert len(authors_found) == 20

    def test_should_save_author_with_id(self, db_test):
        author_repository = AuthorMySQLRepository()
        author = AuthorFactory.build(name="Fowler")

        assert author.id is None

        author_saved = author_repository.save(author)

        assert author_saved.id
        assert "Fowler" == author_saved.name
