from application import app
from controller.response.api import ApiResponse
from model.repository import ReviewRepository
from model.entity import Review
from flask import request

repository = ReviewRepository()

@app.route("/api/reviews/movie/<code>", methods=["GET"])
def listReview(code):
    reviews = repository.findByMovieCode(movie_code=code)
    reviews = [review.toDic() for review in reviews] # List Comprehension
    api = ApiResponse(data=reviews)
    status = 200
    if len(reviews) == 0:
        status = 204
    return api.toDic(), status

@app.route("/api/reviews/<id>", methods=["GET"])
def findReviewById(id):
    # TODO: Validar campos
    api = None
    status = 200
    try:
        data = repository.findById(id)
        api = ApiResponse(data=data.toDic())
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 409
    return api.toDic(), status

@app.route("/api/reviews", methods=["POST"])
def createReview():
    api = None
    status = 201
    try:
        data = request.get_json(force=True)
        # TODO: Validar datos
        if data.get("name") == None:
            api = ApiResponse(message="El nombre es un campo obligatorio")
            status = 409
        else:
            review = Review(
                name=data.get("name"),
                email=data.get("email"),
                description=data.get("description"),
                rating=data.get("rating"),
                movie_code=data.get("code")
            )
            repository.insert(review)
            api = ApiResponse(data=True)
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 409
    return api.toDic(), status

@app.route("/api/reviews/<id>", methods=["PUT"])
def updateReview(id):
    api = None
    status = 200
    try:
        data = request.get_json(force=True)
        # TODO: Validar datos
        review = Review(
            id=id,
            name=data.get("name"),
            email=data.get("email"),
            description=data.get("description"),
            rating=data.get("rating"),
            movie_code=data.get("code")
        )
        repository.update(review)
        api = ApiResponse(data=True)
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 409
    return api.toDic(), status

@app.route("/api/reviews/<id>", methods=["DELETE"])
def deleteReview(id):
    api = None
    status = 200
    try:
        # TODO: Validar campos
        repository.delete(id)
        api = ApiResponse(data=True)
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 409
    return api.toDic(), status

