from application import app
from model.repository import MovieRepository
from model.entity import Movie
from controller.response.api import ApiResponse
from flask import request
from MySQLdb import IntegrityError

repository = MovieRepository()

@app.route("/api/movies", methods=["GET"])
def list():
    movies = repository.findAll()
    response = []
    for movie in movies:
        response.append(movie.toDic())

    api = ApiResponse(data=response)

    return api.toDic(), 200

@app.route("/api/movies/<code>", methods=["GET"])
def findByCode(code):
    api = None
    status = 200
    try:
        movie = repository.findByCode(code)

        api = ApiResponse(data=movie.toDic())
    except Exception as ex:
        status = 400
        api = ApiResponse(message=str(ex))

    return api.toDic(), status

@app.route("/api/movies", methods=["POST"])
def create():
    api = None
    status = 201
    try:
        code = request.json["code"]
        name = request.json["name"]
        image = request.json["image_url"]
        year = request.json["year"]

        movie = Movie(code, name, image_url=image, year= year)
        repository.insert(movie)

        api = ApiResponse()
    except IntegrityError as ex :
        status = 400
        if ex.code == 1062:
            api = ApiResponse(message="Ya existe una pelicula con este codigo")
        else:
            api = ApiResponse(message=str(ex))
    except Exception as ex:
        status = 400
        api = ApiResponse(message=str(ex))

    return api.toDic(), status