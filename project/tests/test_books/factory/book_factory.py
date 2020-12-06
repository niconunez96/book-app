from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence, SubFactory

from books.domain.book import Book
from database import db
from tests.test_books.factory.author_factory import AuthorFactory


class BookFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Book
        sqlalchemy_session = db.session

    title = Sequence(lambda a: "Title {}".format(a+1))
    description = Sequence(lambda a: "Description {}".format(a+1))
    author_id = SubFactory(AuthorFactory)
    author = SubFactory(AuthorFactory)
