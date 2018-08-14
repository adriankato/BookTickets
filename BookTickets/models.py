from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Movie(db.Model):
    """Creates a table for named Movie"""

    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    customers = db.relationship("Customer", backref="movie", lazy=True)

    def add_customer(self,name):
        # Add customer to movie
        c = Customer(name=name, movie_id=self.id)
        db.session.add(c)
        db.session.commit()

class Customer(db.Model):
    """Creates a table named Customer"""

    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    