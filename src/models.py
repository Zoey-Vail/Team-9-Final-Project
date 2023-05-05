# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={"expire_on_commit": False})

#class utility(db.Model):
    #current_username = db.Column(db.Integer, primary_key=True, nullable=False)
    #current_forum_id = db.Column(db.Integer)
    #ogged_in = db.Column(db.Boolean)

    #def __init__(self, curr_user, curr_for_ID, logged):
        #self.current_username = curr_user
        #self.current_forum_id = curr_for_ID
        #self.logged_in = logged


class account(db.Model):
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    website = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    major = db.Column(db.String(255), nullable=False)
    concentration = db.Column(db.String(255), nullable=False)
    #This below is the login state for the user when traversing the website
    logged_In = db.Column(db.Boolean, default=False,nullable=False)

    def __init__(self, _uName, _pWord, _eMail, _age, _wSite, _gender, _major, _concentration):
        self.username = _uName
        self.password = _pWord
        self.email = _eMail
        self.age = _age
        self.website = _wSite
        self.gender = _gender
        self.major = _major
        self.concentration = _concentration
        self.logged_In = True

class forums(db.Model):
    forum_id = db.Column(db.Integer, primary_key=True)
    forum_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    
    def __init__(self, _forID, _forName, _descript):
        self.forum_id = _forID
        self.forum_name = _forName
        self.description = _descript

class discussion(db.Model):
    discuss_ID = forum_id = db.Column(db.Integer, primary_key=True, nullable=False)
    creator_username = db.Column(db.String(255), nullable=False)
    parent_forum_ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.String(255))
    majors = db.Column(db.String(255))
    classes = db.Column(db.String(255))
    companies = db.Column(db.String(255))

    def __init__(self, _discussID, _creator, _parentForID, _title, _content, _tag, _major, _class, _company):
        self.discuss_ID = _discussID
        self.creator_username = _creator
        self.parent_forum_ID
        self.title = _title
        self.content = _content
        self.tags = _tag
        self.majors = _major
        self.classes = _class
        self.companies = _company
