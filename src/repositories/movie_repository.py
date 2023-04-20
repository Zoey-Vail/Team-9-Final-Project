from src.models import db, Movie
id_counter = 0
class MovieRepository:
    def create_data(self):
        db.create_all()
        return None
    
    def get_all_movies(self):
        # TODO get all movies from the DB
        mov = Movie.query.all()
        print(mov)
        return mov

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return None

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_movie = Movie(_id = id_counter, ttl = title, direc = director, rtng = rating)
        id_counter + 1
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
