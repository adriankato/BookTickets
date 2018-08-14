from flask import Flask, render_template, request, jsonify
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://@localhost:5432/movietickets'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    """ Main page. Show all Movies to user."""
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)

@app.route("/book", methods=["POST"])
def book():
    """Book a Movie."""
    #Get information from form to book
    name = request.form.get("name")
    try:
        movie_id = int(request.form.get("movie_id"))
    except ValueError:
        return render_template("error.html", message="Invalid movie.")

    #Make sure the movie exists
    movie = Movie.query.get(movie_id)
    if movie is None:
        return render_template("error.html", message="No such movie with that id.")
    
    #Add customer
    movie.add_customer(name)
    return render_template("success.html")

@app.route("/movies")
def movies():
    """List all movies."""
    movies = Movie.query.all()
    return render_template("movies.html", movies=movies)

@app.route("/movies/<int:movie_id>")
def movie(movie_id):
    """List details about a movie."""

    #Make sure movie exists.
    movie = Movie.query.get(movie_id)
    if movie is None:
        return render_template("error.html", message="Movie doesn't exist")

    #Get all customers.
    customers = movie.customers
    return render_template("movie.html", movie=movie, customers=customers)

@app.route("/cancel", methods=["DELETE"])
def cancel(customer, movie_id):
    """Cancel booking"""
    