from datetime import datetime
import pytest
from mock import Mock

from books.application.book import BookFinder, BooksFinder
from books.domain import EntityNotFound

from tests.test_books.factory.book_factory import BookFactory


class TestBookFinder:

    def test_should_return_book_found_by_repository(self):
        stub_repository = Mock(
            find_by_id=Mock(return_value=BookFactory.build(
                id=1,
                title="title",
                description="desc",
                created=datetime(2020, 9, 11),
            ))
        )
        book_finder = BookFinder(book_repository=stub_repository)

        book_found = book_finder.execute(book_id=1)

        assert {
            'id': 1,
            'title': "title",
            'description': "desc",
            'created': "2020-09-11 00:00:00",
        } == book_found

    def test_should_return_entity_not_found_when_id_does_not_exist(self):
        stub_repository = Mock(
            find_by_id=Mock(side_effect=EntityNotFound)
        )
        book_finder = BookFinder(book_repository=stub_repository)

        with pytest.raises(EntityNotFound):
            book_finder.execute(book_id=1)


class TestBooksFinder:

    def test_should_return_books_found_by_repository(self):
        stub_repository = Mock(
            find_all=Mock(return_value=[
                BookFactory.build(
                    id=1,
                    title="title1",
                    description="desc",
                    created=datetime(2020, 9, 11),
                ),
                BookFactory.build(
                    id=2,
                    title="title2",
                    description="desc",
                    created=datetime(2020, 9, 11),
                ),
                BookFactory.build(
                    id=3,
                    title="title3",
                    description="desc",
                    created=datetime(2020, 9, 11),
                ),
            ])
        )
        books_finder = BooksFinder(book_repository=stub_repository)

        books_found = books_finder.execute()

        assert [
            {
                'id': 1,
                'title': "title1",
                'description': "desc",
                'created': "2020-09-11 00:00:00",
            },
            {
                'id': 2,
                'title': "title2",
                'description': "desc",
                'created': "2020-09-11 00:00:00",
            },
            {
                'id': 3,
                'title': "title3",
                'description': "desc",
                'created': "2020-09-11 00:00:00",
            },
        ] == books_found
