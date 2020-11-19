import json

from project.controller import app
from project.books.application.books_finder import BooksFinder, BookFinder
from project.books.infrastructure.book_mysql_repository import BookMySQLRepository


@app.route('/api/v1/books/')
def find_all():
    books_finder = BooksFinder(BookMySQLRepository())
    return json.dumps(books_finder.execute())

@app.route('/api/v1/books/<book_id>/')
def find_by_id(book_id: int):
    book_finder = BookFinder(BookMySQLRepository())
    return json.dumps(book_finder.execute(book_id))
