# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={"expire_on_commit": False})

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, _id, ttl, direc, rtng):
        self.movie_id = _id
        self.title = ttl
        self.director = direc
        self.rating = rtng
