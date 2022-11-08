from application import app
from model.repository import MovieRepository
from model.entity import Movie
from controller.api import ApiResponse
from flask import jsonify, request

repository = MovieRepository()

@app.route("/api/movies", methods=["GET"])
def list():
    response = None
    status_code = 200
    try:
        movies = [movie.json() for movie in repository.findAll()]
        response = ApiResponse(data=movies)
        if len(movies) == 0:
            status_code = 204
    except Exception as e:
        response = ApiResponse(message=str(e))
        status_code = 400

    return jsonify(response.json()), status_code


@app.route("/api/movies/<code>", methods=["GET"])
def findByCode(code):
    response = None
    status_code = 200
    try:
        response = ApiResponse(data=repository.findByCode(code).json())
    except Exception as e:
        response = ApiResponse(message=str(e))
        status_code = 404

    return jsonify(response.json()), status_code

@app.route("/api/movies", methods=["POST"])
def create():
    response = None
    status_code = 201
    try:
        json = request.get_json(force=True)

        if json.get("code") is None:
            response = ApiResponse(message="Codigo de la pelicula es obligatorio")
            status_code = 400
        elif json.get("name") is None:
            response = ApiResponse(message="Nombre de la pelicula es obligatorio")
            status_code = 400
        else:
            movie = Movie(
                code=json.get("code"),
                name=json.get("name"),
                image_url=json.get("image_url"),
                year=json.get("year"))
            repository.insert(movie)
            response = ApiResponse(data=True)
    except Exception as e:
        response = ApiResponse(message=str(e))
        status_code = 400
    return jsonify(response.json()), status_code