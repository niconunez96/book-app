from datetime import datetime
from database import db
from sqlalchemy.orm import relationship

from books.domain.author import Author


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = relationship('Author')

    def __init__(self, title: str, description: str, author: Author, **kwargs):
        super(Book, self).__init__(**kwargs)
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return 'Book <id {}>'.format(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created': str(self.created),
        }
