class Movie:
    def __init__(self, code, name, image_url = None, year = None) -> None:
        self.code = code
        self.name = name
        self.image_url = image_url
        self.year = year

    def toDic(self):
        return {
            "code": self.code,
            "name": self.name,
            "image_url": self.image_url,
            "year": self.year
        }
    

class Review:
    def __init__(self, name, email, description, rating, movie_code, id = None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.description = description
        self.rating = rating
        self.code = movie_code
