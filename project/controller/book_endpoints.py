from flask import jsonify, Blueprint
from books.application.book import BooksFinder, BookFinder
from books.domain import EntityNotFound
from books.infrastructure.book_mysql_repository import BookMySQLRepository  # noqa
from controller.response import Response


books = Blueprint("books", __name__, url_prefix="/api/v1/books")


@books.route('/', methods=['GET'])
def find_all():
    books_finder = BooksFinder(BookMySQLRepository())
    return Response(jsonify(books_finder.execute()), 200)


@books.route('/<int:book_id>/', methods=['GET'])
def find_by_id(book_id: int):
    try:
        book_finder = BookFinder(BookMySQLRepository())
        return jsonify(book_finder.execute(book_id)), 200
    except EntityNotFound:
        return Response(
            {
                'error': "NOT_FOUND",
                'description': "Resource requested does not exist",
            },
            404,
        )
