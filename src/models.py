# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={"expire_on_commit": False})

class account(db.Model):
    username = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    website = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    major = db.Column(db.String(255), nullable=False)
    concentration = db.Column(db.String(255), nullable=False)

    def __init__(self, _uName, _pWord, _eMail, _age, _wSite, _gender, _major, _concentration):
        self.username = _uName
        self.password = _pWord
        self.email = _eMail
        self.age = _age
        self.website = _wSite
        self.gender = _gender
        self.major = _major
        self.concentration = _concentration

class forums(db.Model):
    forum_id = db.Column(db.Integer, primary_key=True)
    forum_name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    
    def __init__(self, _forID, _forName, _descript):
        self.forum_id = _forID
        self.forum_name = _forName
        self.description = _descript
        