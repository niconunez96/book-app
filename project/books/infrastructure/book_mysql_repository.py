from typing import List

from database import db
from books.domain import (
    CouldNotSaveEntity,
    EntityNotFound,
)
from books.domain.book_repository import BookRepository
from books.domain.book import Book
from books.domain.author import Author


class BookMySQLRepository(BookRepository):

    def find_all(self) -> List[Book]:
        return db.session.query(Book).all()

    def find_by_id(self, id: int) -> Book:
        entity = db.session.query(Book).get(id)
        if not entity:
            raise EntityNotFound
        return entity

    def find_by_author(self, author_id: int) -> List[Book]:
        return db.session.query(Book).filter(Book.author_id == author_id).all()

    def save(self, entity: Book) -> Book:
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except Exception:
            db.session.rollback()
            raise CouldNotSaveEntity
