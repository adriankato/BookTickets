import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://@localhost:5432/movietickets'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("movies.csv")
    reader = csv.reader(f)
    for title, location, duration in reader:
        movie = Movie(title=title, location=location, duration=duration)
        db.session.add(movie)
        print(f"Added movie: {title} at {location} lasting {duration} minutes")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()