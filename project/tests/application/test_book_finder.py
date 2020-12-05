import pytest
from mock import Mock

from books.domain.book import Book
from books.application.books_finder import BookFinder, BooksFinder
from books.domain import EntityNotFound


class TestBookFinder:

    def test_should_return_book_found_by_repository(self):
        stub_repository = Mock(
            find_by_id=Mock(return_value=Book("title", "desc"))
        )
        book_finder = BookFinder(book_repository=stub_repository)

        book_found = book_finder.execute(book_id=1)

        assert {
            'id': None,
            'title': "title",
            'description': "desc",
            'created': 'None',
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
                Book("title1", "desc"),
                Book("title2", "desc"),
                Book("title3", "desc"),
            ])
        )
        books_finder = BooksFinder(book_repository=stub_repository)

        books_found = books_finder.execute()

        assert [
            {
                'id': None,
                'title': "title1",
                'description': "desc",
                'created': 'None',
            },
            {
                'id': None,
                'title': "title2",
                'description': "desc",
                'created': 'None',
            },
            {
                'id': None,
                'title': "title3",
                'description': "desc",
                'created': 'None',
            },
        ] == books_found
