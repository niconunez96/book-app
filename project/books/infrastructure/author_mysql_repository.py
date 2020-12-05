from typing import List

from database import db
from books.domain import (
    CouldNotSaveEntity,
    EntityNotFound,
)
from books.domain.author_repository import AuthorRepository
from books.domain.author import Author


class AuthorMySQLRepository(AuthorRepository):

    def find_all(self) -> List[Author]:
        return db.session.query(Author).all()

    def find_by_id(self, id: int) -> Author:
        entity = db.session.query(Author).get(id)
        if not entity:
            raise EntityNotFound
        return entity

    def save(self, entity: Author) -> Author:
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except Exception:
            db.session.rollback()
            raise CouldNotSaveEntity
