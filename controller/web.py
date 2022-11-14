from flask import render_template
from application import app

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/busqueda.html")
def busqueda():
    return render_template("busqueda.html")

@app.route("/buscar")
def buscar():
    return render_template("busqueda.html")

@app.route("/detalle/<id>")
def detalle(id):
    return render_template("detalle.html")

