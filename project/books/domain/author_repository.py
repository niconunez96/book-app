from typing import List
from books.domain.author import Author


class AuthorRepository:

    def find_all(self) -> List[Author]:
        raise NotImplementedError

    def find_by_id(self, id: int) -> Author:
        raise NotImplementedError

    def save(self, entity: Author) -> Author:
        raise NotImplementedError
