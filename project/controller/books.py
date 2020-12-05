from flask import jsonify, Blueprint, request
from books.application.books_finder import BooksFinder, BookFinder
from books.application.book_creator import BookCreator
from books.domain.book_repository import EntityNotFound
from books.infrastructure.book_mysql_repository import BookMySQLRepository  # noqa
from controller import Response


books = Blueprint("books", __name__, url_prefix="/api/v1/books")


@books.route('/', methods=['GET'])
def find_all():
    books_finder = BooksFinder(BookMySQLRepository())
    return Response(jsonify(books_finder.execute()), 200)


@books.route('/', methods=['POST'])
def create():
    body = request.json
    book_creator = BookCreator(BookMySQLRepository())
    book_id = book_creator.execute(book_body=body)
    return Response(
        {'resource_url': "/api/v1/books/{}/".format(book_id)},
        201,
    )


@books.route('/<book_id>/', methods=['GET'])
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
