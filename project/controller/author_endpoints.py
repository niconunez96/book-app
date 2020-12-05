from flask import Blueprint, jsonify, request
from books.application.author_finder import AuthorFinder, AuthorsFinder
from books.application.author_creator import AuthorCreator
from books.domain import EntityNotFound
from books.infrastructure.author_mysql_repository import AuthorMySQLRepository
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
    book_creator = AuthorCreator(AuthorMySQLRepository())
    book_id = book_creator.execute(author_body=body)
    return Response(
        {'resource_url': "/api/v1/authors/{}/".format(book_id)},
        201,
    )
