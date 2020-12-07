from datetime import datetime
from freezegun import freeze_time
import json
from tests.test_books.factory.author_factory import AuthorFactory
from tests.test_books.factory.book_factory import BookFactory


@freeze_time(datetime(2020, 9, 11))
class TestAuthorEndpoints:

    def test_should_create_author(self, db_test, client):
        request_body = {
            'name': "Fowler",
            'biography': "Some example biography",
        }

        response = client.post(
            "/api/v1/authors/",
            mimetype='application/json',
            data=json.dumps(request_body),
        )

        assert response.status == "201 CREATED"
        assert response.get_json() == {
            "resource_url": "/api/v1/authors/1/"
        }

    def test_returns_author_with_specified_id(self, db_test, client):
        AuthorFactory.create(id=2, name="Martin", biography="Biography")
        response = client.get("/api/v1/authors/2/")

        assert response.status == "200 OK"
        assert response.get_json() == {
            'id': 2,
            'name': "Martin",
            'biography': "Biography",
            'created': "2020-09-11 00:00:00",
        }

    def test_returns_all_authors_saved(self, db_test, client):
        AuthorFactory.create_batch(size=3)
        response = client.get("/api/v1/authors/")

        assert response.status == "200 OK"
        assert response.get_json() == [
            {
                'id': 1,
                'name': "John Doe 1",
                'biography': "Biography 1",
                'created': "2020-09-11 00:00:00",
            },
            {
                'id': 2,
                'name': "John Doe 2",
                'biography': "Biography 2",
                'created': "2020-09-11 00:00:00",
            },
            {
                'id': 3,
                'name': "John Doe 3",
                'biography': "Biography 3",
                'created': "2020-09-11 00:00:00",
            },
        ]

    def test_should_return_not_found_when_author_does_not_exist(
        self,
        db_test,
        client
    ):
        response = client.get("/api/v1/authors/-1/")

        assert response.status == "404 NOT FOUND"

    def test_should_create_book_related_with_author_specified(
        self,
        db_test,
        client,
    ):
        author = AuthorFactory.create(id=1)
        request_body = {
            'title': "New book",
            'description': "New description",
        }

        response = client.post(
            "/api/v1/authors/{}/books/".format(author.id),
            mimetype='application/json',
            data=json.dumps(request_body),
        )

        assert response.status == "201 CREATED"
        assert response.get_json() == {
            "resource_url": "/api/v1/books/1/"
        }

    def test_should_return_not_found_when_create_book_with_unexistent_author(
        self,
        db_test,
        client
    ):
        request_body = {
            'title': "New book",
            'description': "New description",
        }

        response = client.post(
            "/api/v1/authors/-1/books/",
            mimetype='application/json',
            data=json.dumps(request_body),
        )

        assert response.status == "404 NOT FOUND"

    def test_should_return_books_related_with_specified_author(
        self,
        db_test,
        client,
    ):
        author = AuthorFactory.create(id=1)
        BookFactory.create_batch(
            size=2,
            author=author,
            author_id=author.id,
        )
        response = client.get("/api/v1/authors/1/books/")

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
        ]

    def test_should_return_not_found_when_request_books_of_unexistent_author(
        self,
        db_test,
        client
    ):
        response = client.get("/api/v1/authors/-1/books/")

        assert response.status == "404 NOT FOUND"
