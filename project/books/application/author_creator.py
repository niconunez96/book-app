from books.domain.author_repository import AuthorRepository
from books.domain.author import Author


class AuthorCreator:

    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, author_body: dict) -> int:
        new_author = Author(author_body['name'], author_body['biography'])
        author_id = self.author_repository.save(new_author)
        return author_id
