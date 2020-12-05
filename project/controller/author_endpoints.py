from flask import Blueprint, jsonify, request
from books.application.author_finder import AuthorFinder, AuthorsFinder
from books.application.author_creator import AuthorCreator
from books.application.book_creator import BookCreator, AuthorDoesNotExist
from books.domain import EntityNotFound
from books.infrastructure.author_mysql_repository import AuthorMySQLRepository
from books.infrastructure.book_mysql_repository import BookMySQLRepository
from controller.response import Response


authors = Blueprint("author", __name__, url_prefix="/api/v1/authors")


@authors.route("/", methods=['GET'])
def find_all():
    authors_finder = AuthorsFinder(AuthorMySQLRepository())
    return Response(jsonify(authors_finder.execute()), 200)


@authors.route("/<int:author_id>/", methods=['GET'])
def find_by_id(author_id: int):
    try:
        author_finder = AuthorFinder(AuthorMySQLRepository())
        return Response(jsonify(author_finder.execute(author_id)), 200)
    except EntityNotFound:
        return Response(
            {
                'error': "NOT_FOUND",
                'description': "Resource requested does not exist",
            },
            404,
        )


@authors.route("/", methods=['POST'])
def create():
    body = request.json
    author_creator = AuthorCreator(AuthorMySQLRepository())
    author_id = author_creator.execute(author_body=body)
    return Response(
        {'resource_url': "/api/v1/authors/{}/".format(author_id)},
        201,
    )


@authors.route("/<int:author_id>/books/", methods=['POST'])
def add_book(author_id: int):
    body = request.json
    book_creator = BookCreator(
        AuthorMySQLRepository(),
        BookMySQLRepository(),
    )
    try:
        book_id = book_creator.execute(author_id, book_body=body)
        return Response(
            {"resource_url": "/api/v1/books/{}".format(book_id)},
            201,
        )
    except AuthorDoesNotExist:
        return Response(
            {
                'error': "NOT_FOUND",
                'description': "Resource requested does not exist",
            },
            404,
        )
