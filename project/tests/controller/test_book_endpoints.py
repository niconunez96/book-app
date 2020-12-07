from datetime import datetime
from freezegun import freeze_time

from tests.test_books.factory.book_factory import BookFactory


@freeze_time(datetime(2020, 9, 11))
class TestBookEndpoints:

    def test_returns_empty_list_when_there_is_no_book(self, db_test, client):
        response = client.get("/api/v1/books/")

        assert response.status == "200 OK"
        assert response.get_json() == []

    def test_returns_all_books_saved(self, db_test, client):
        BookFactory.create_batch(size=3)
        response = client.get("/api/v1/books/")

        assert response.status == "200 OK"
        assert response.get_json() == [
            {
                'id': 1,
                'title': "Title 1",
                'description': "Description 1",
                'created': "2020-09-11 00:00:00",
            },
            {
                'id': 2,
                'title': "Title 2",
                'description': "Description 2",
                'created': "2020-09-11 00:00:00",
            },
            {
                'id': 3,
                'title': "Title 3",
                'description': "Description 3",
                'created': "2020-09-11 00:00:00",
            },
        ]

    def test_returns_book_with_specific_id(self, db_test, client):
        BookFactory.create(id=4, title="Bla", description="Desc")
        response = client.get("/api/v1/books/4/")

        assert response.status == "200 OK"
        assert response.get_json() == {
            'id': 4,
            'title': "Bla",
            'description': "Desc",
            'created': "2020-09-11 00:00:00",
        }

    def test_should_return_not_found_when_book_id_does_not_exist(
        self,
        db_test,
        client,
    ):
        response = client.get("/api/v1/books/-1/")

        assert response.status == "404 NOT FOUND"
