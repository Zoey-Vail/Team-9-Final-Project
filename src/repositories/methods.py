from src.models import db, account, forum
id_counter = 0
class accMethods:
    def create_data(self):
        db.create_all()
        return None
    
    def verify_account(self, username, password):
        #This is the verification for the database 
        print('hello')
        check = account.query.filter_by(username = username).first()
        if (check.password == password):
            return True
        elif (check.password != password):
            return False

    def get_account(self, _usename):
        # TODO gets a single account from the database
        result = account.query.filter_by(username = _usename).first()
        return result
    
    def account_exists(self, username):
        try:
            if(username == account_methods.get_account(username).username):
                return True
        except Exception as err:
            return False

    def create_account(self, username, password, email, age, website, gender, major, concentration):
        # TODO Creates a new account

        new_account = account(_uName = username, _pWord = password, _eMail = email, _age = age, _wSite = website, _gender = gender, _major = major, _concentration = concentration)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def create_forums(self):
        # TODO get a single movie from the DB using the ID
        global counter
        counter = counter + 1
        new_forum = forum(_forName = ("Forum "+ str(counter)), _descript = ("this is forum" + str(counter)))
        db.session.add(new_forum)
        db.session.commit()
        return new_forum

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None

# Singleton to be used in other modules
account_methods = accMethods()