from datetime import datetime
from database import db


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, title: str, description: str, created: datetime):
        self.title = title
        self.description = description
        self.created = created

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created': str(self.created),
        }
