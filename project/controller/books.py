from flask import jsonify, Blueprint
from books.application.books_finder import BooksFinder, BookFinder
from books.infrastructure.book_mysql_repository import BookMySQLRepository  # noqa


books = Blueprint("books", __name__)


@books.route('/api/v1/books/')
def find_all():
    books_finder = BooksFinder(BookMySQLRepository())
    return jsonify(books_finder.execute()), 200


@books.route('/api/v1/books/<book_id>/')
def find_by_id(book_id: int):
    book_finder = BookFinder(BookMySQLRepository())
    return jsonify(book_finder.execute(book_id)), 200
