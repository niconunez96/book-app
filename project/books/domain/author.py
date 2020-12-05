from datetime import datetime
from database import db


class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    biography = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, name: str, biography: str):
        self.name = name
        self.biography = biography

    def __repr__(self):
        return 'Author <id {}>'.format(self.id)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'biography': self.biography,
            'created': str(self.created),
        }
