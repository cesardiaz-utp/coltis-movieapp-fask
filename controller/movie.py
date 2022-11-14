from application import app
from model.repository import MovieRepository
from model.entity import Movie
from flask import request

repository = MovieRepository()

@app.route("/api/movies", methods=["GET"])
def list():
    return repository.findAll()

@app.route("/api/movies/<code>", methods=["GET"])
def findByCode(code):
    return repository.findByCode(code)

@app.route("/api/movies", methods=["POST"])
def create():
    code = request.json["code"]
    name = request.json["name"]
    image = request.json["image_url"]
    year = request.json["year"]

    movie = Movie(code, name, image_url=image, year= year)
    repository.insert(movie)

    return "{ 'message': 'Muy bien' }", 201