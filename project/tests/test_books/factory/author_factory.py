from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence
from books.domain.author import Author
from database import db


class AuthorFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Author
        sqlalchemy_session = db.session

    name = Sequence(lambda a: "John Doe {}".format(a+1))
    biography = Sequence(lambda a: "Biography {}".format(a+1))
