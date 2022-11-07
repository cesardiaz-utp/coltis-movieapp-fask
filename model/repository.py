from model.entity import Movie, Review


class MovieRepository:
    def insert(movie: Movie) -> None:
        pass

    def findByCode(code: str) -> list:
        pass

    def findAll() -> list:
        pass


class ReviewRepository:
    def insert(review: Review) -> None:
        pass

    def findById(id: int) -> list:
        pass

    def findAll() -> list:
        pass

    def update(review: Review) -> None:
        pass

    def delete(id: int) -> None:
        pass
