from datetime import datetime


class Book:

    id = 1

    def __init__(self, title: str, description: str, created: datetime):
        self.title = title
        self.description = description
        self.created = created

    def __dict__(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created': str(self.created),
        }
