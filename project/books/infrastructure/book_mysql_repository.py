from typing import List

from database import db
from books.domain.book_repository import (
    BookRepository,
    CouldNotSaveEntity,
    EntityNotFound,
)
from books.domain.book import Book


class BookMySQLRepository(BookRepository):

    def find_all(self) -> List[Book]:
        return db.session.query(Book).all()

    def find_by_id(self, id: int) -> Book:
        entity = db.session.query(Book).get(id)
        if not entity:
            raise EntityNotFound
        return entity

    def save(self, entity: Book) -> Book:
        try:
            db.session.add(entity)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise CouldNotSaveEntity
