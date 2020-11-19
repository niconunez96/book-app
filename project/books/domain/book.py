from datetime import datetime


class Book:

    id = 1

    def __init__(self, title: str, description: str, created: datetime):
        self.title = title
        self.description = description
        self.created = created
