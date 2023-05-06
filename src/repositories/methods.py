from src.models import db, account, forums, discussion
import lorem




class accMethods:
    # Creates the database
    def create_data(self):
        db.create_all()
        return None
    
    # Clears data from all tables
    def clear_data(session):
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

    #This is the verification for the database 
    def verify_account(self, username, password):
        check = account.query.filter_by(username = username).first()
        if (check.password == password):
            return True
        elif (check.password != password):
            return False
    # gets a single account from the database
    def get_account(self, _usename):
        result = account.query.filter_by(username = _usename).first()
        return result
    
    #This method checks if the account exists and if it does then will return True if not False
    def account_exists(self, username):
        try:
            if(username == account_methods.get_account(username).username):
                return True
        except Exception as err:
            return False
        
        
#-------------------------------------------------- Authorization Section of Program--------------------------------------------------
   
    #This method shows whether or not an account is currently authorized accross the website
    def account_Authorize_check(self, username):
        try:
            authorized = account_methods.get_account(username).logged_In
            if(authorized == True):
                return True
            else:
                return False
        except Exception as err:
            raise Exception('Error has been thrown because login authorization does not work')
    
    #This method authorizes an account to go through the site after login. 
    def account_Authorization(self, username):
        try:
            check = account.query.filter_by(username = username).first()
            check.logged_In = True
            db.session.commit()
        except Exception as err:
            raise Exception('Error has been thrown because login authorization does not work')

    #This method unauthorizes an account to go through the site after they are done. 
    def account_unAuthorization(self, username):
        try:
            check = account.query.filter_by(username = username).first()
            check.logged_In = False
            db.session.commit()
        except Exception as err:
            raise Exception('Error has been thrown because login authorization does not work')

#-------------------------------------------------- Authorization Section of Program Above--------------------------------------------------

    # Gets the amount of forums in the forum table
    def get_number_of_forums(self):
        try:
            return int(forums.query.count())
        except Exception as err:
            return 0
    # Gets the forum object with forum_id matching id parameter
    def get_forum_by_id(self, id):
        forum_to_return = forums.query.filter_by(forum_id = id).first()
        return forum_to_return
    # adds all forums in the database to an array and returns the array
    def add_forums_to_array(self, forum_arr):
        query = forums.query.all()
        for row in query:
            forum_arr.append(row)
        return forum_arr
    # Creates an example forum and adds it to the database
    def create_forums(self, forum_id):
        descript = lorem.sentence()
        descript_split = descript.split()
        # creates a new forum with the forum_id paramater, a name containing the first word of the description, and a description from the lorem generator
        new_forum = forums(_forID = forum_id, _forName = ("Forum "+ descript_split[0]), _descript = descript)
        db.session.add(new_forum)
        db.session.commit()
        return new_forum
    
    def get_last_discussion_ID(self):
        post_amount = 0
        try:
            post_amount = int(forums.query.count())
        except Exception as err:
            return post_amount
        last_post = discussion.query.order_by(discussion.discuss_ID.desc()).first()
        print('last= '+ str(last_post.discuss_ID))
        return last_post.discuss_ID

    def get_post_by_ID(self, post_ID):
        post_to_return = discussion.query.filter_by(discuss_ID = post_ID).first()
        return post_to_return


    def get_posts_by_forum(self, forum_id):
        post_arr = []
        query = discussion.query.filter_by(parent_forum_ID = forum_id)
        for row in query:
            post_arr.append(row)
        return post_arr

    def get_posts_by_user(self, user_ID):
        post_arr = []
        query = discussion.query.filter_by(creator_username = user_ID)
        for row in query:
            post_arr.append(row)
        return post_arr
        
    # Creates account from parameters given and adds it to the database
    def create_account(self, username, password, email, age, website, gender, major, concentration):
        new_account = account(_uName = username, _pWord = password, _eMail = email, _age = age, _wSite = website, _gender = gender, _major = major, _concentration = concentration)
        db.session.add(new_account)
        db.session.commit()
        return new_account


#object containing the methods used in the app.py
account_methods = accMethods()
