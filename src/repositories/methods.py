from src.models import db, account
id_counter = 0
class accMethods:
    def create_data(self):
        db.create_all()
        return None
    
    def get_all_movies(self):
        # TODO get all movies from the DB
        return None

    def get_account(self, _usename):
        # TODO get a single movie from the DB using the ID
        result = account.query.filter_by(username = _usename).first()
        return result

    def create_account(self, username, password, email, age, website, gender, major, concentration):
        # TODO create a new movie in the DB

        new_account = account(_uName = username, _pWord = password, _eMail = email, _age = age, _wSite = website, _gender = gender, _major = major, _concentration = concentration)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None

# Singleton to be used in other modules
account_methods = accMethods()
