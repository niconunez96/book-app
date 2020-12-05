from books.domain.author_repository import AuthorRepository


class AuthorFinder:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, id: int) -> dict:
        return self.author_repository.find_by_id(id).to_dict()


class AuthorsFinder:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self) -> dict:
        return [
            author.to_dict()
            for author in self.author_repository.find_all()
        ]
