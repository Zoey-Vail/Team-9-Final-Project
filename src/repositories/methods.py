from src.models import db, account, forums, discussion, comment
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
    def account_deAuthorization(self, username):
        try:
            check = account.query.filter_by(username = username).first()
            check.logged_In = False
            db.session.commit()
        except Exception as err:
            print('Account does not exist')

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
    
      # creates a discussion post in the parent forum matching the forum_id
    def create_post(self, post_ID, creator_username, parent_forum, parent_forum_name, title, content, tags, majors, classes, companies):
        new_discussion = discussion(_discussID = post_ID, _creator = creator_username, _parentForID = parent_forum, _forum_posted_to = parent_forum_name, _title = title, _content = content, _tag = tags, _major = majors, _class = classes, _company = companies)
        db.session.add(new_discussion)
        db.session.commit()
        return new_discussion
    #Returns the post ID of the last post in the discussion database
    def get_last_discussion_ID(self):
        post_amount = 0
        try:
            post_amount = int(forums.query.count())
        except Exception as err:
            return post_amount
        try:
            last_post = discussion.query.order_by(discussion.discuss_ID.desc()).first()
            return last_post.discuss_ID
        except Exception as err:
            return 0
    #returnst the post with the matching post_ID
    def get_post_by_ID(self, post_ID):
        post_to_return = discussion.query.filter_by(discuss_ID = post_ID).first()
        return post_to_return

    # returns an array containing all posts with parent_forum_ID matching the forum_ID parameter
    def get_posts_by_forum(self, forum_id):
        post_arr = []
        query = discussion.query.filter_by(parent_forum_ID = forum_id)
        for row in query:
            post_arr.append(row)
        return post_arr

    # returns an array containing all posts with creator_username matching the user_ID parameter
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
    
    # returns the ID of the last reply
    def get_last_reply_ID(self):
        post_amount = 0
        try:
            post_amount = int(comment.query.count())
        except Exception as err:
            return post_amount
        try:
            last_reply = comment.query.order_by(comment.comment_ID.desc()).first()
            return last_reply.comment_ID
        except Exception as err:
            return 0
        
    # creates a reply to a post given the parameters
    def create_reply(self, comment_ID, content, discussion, creator):
        new_comment = comment(_comment_ID = comment_ID, _reply_content = content, _parent_discussion_ID = discussion, _creator_username = creator)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment
    
    # returns an array all the replies to the post matching the post_ID
    def get_replies_to_post(self, post_ID):
        reply_arr = []
        query = comment.query.filter_by(parent_discussion_ID = post_ID)
        for row in query:
            reply_arr.append(row)
        return reply_arr
    
    # Automatically generates a forum post corresponding to fourum_id, adds it to the database, and returns it
    def generate_post(self, forum_id):
        post_ID = int(account_methods.get_last_discussion_ID()) + 1
        title = lorem.sentence()
        content = (lorem.sentence() + " " + lorem.sentence() + " " + lorem.sentence())
        creator = "Guest"
        parent_forum = account_methods.get_forum_by_id(forum_id)
        auto_post = discussion(post_ID, creator, forum_id, parent_forum.forum_name, title, content, '', '', '', '')
        db.session.add(auto_post)
        db.session.commit()
        return auto_post
    
    def search_posts(self, content):
        found_posts = discussion.query.filter(discussion.content.like('%' + content + '%')).all()
        return found_posts


#object containing the methods used in the app.py
account_methods = accMethods()
