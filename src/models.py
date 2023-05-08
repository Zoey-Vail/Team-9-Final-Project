# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={"expire_on_commit": False})

class tempUsername:
    def __init__(self, username:str):
        self._currentUsername = username
    
    def setCurrentUsername(self, username:str):    
         self._currentUsername = username

    def getCurrentUsername(self):
        return self._currentUsername
    

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
    discuss_ID = db.Column(db.Integer, primary_key=True, nullable=False)
    creator_username = db.Column(db.String(255), nullable=False)
    parent_forum_ID = db.Column(db.Integer, primary_key=True)
    parent_forum_name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    tags = db.Column(db.String(255))
    majors = db.Column(db.String(255))
    classes = db.Column(db.String(255))
    companies = db.Column(db.String(255))

    def __init__(self, _discussID, _creator, _parentForID,_forum_posted_to, _title, _content, _tag, _major, _class, _company):
        self.discuss_ID = _discussID
        self.creator_username = _creator
        self.parent_forum_ID = _parentForID
        self.parent_forum_name = _forum_posted_to
        self.title = _title
        self.content = _content
        self.tags = _tag
        self.majors = _major
        self.classes = _class
        self.companies = _company

class comment(db.Model):
    comment_ID = db.Column(db.Integer, primary_key=True, nullable=False)
    reply_content = db.Column(db.String(255), nullable=False)
    parent_discussion_ID = db.Column(db.Integer, primary_key=True)
    creator_username = db.Column(db.String(255), nullable=False)

    def __init__(self, _comment_ID, _reply_content, _parent_discussion_ID, _creator_username):
        self.comment_ID = _comment_ID
        self.reply_content = _reply_content
        self.parent_discussion_ID = _parent_discussion_ID
        self.creator_username = _creator_username