from flask import Flask, abort, redirect, render_template, request, send_from_directory, url_for
from src.repositories.methods import account_methods
from src.models import db
from src.models import tempUsername

app = Flask(__name__, template_folder='templates', static_folder='StaticFile')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:PASSWORDCHANGEHERE@localhost:3306/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
if_Create_Account = False
forum_list = []

#Define a route for the homepage
with app.app_context():
    #------------!!!-uncomment line below and run app.py to clear the database-!!!------------
    #account_methods.clear_data()
    #-----------------------------------------------------------------------------------------
    db.create_all()
    forum_list = []
    account_methods.create_data()
    if account_methods.get_number_of_forums() == 0:
        for i in range(3):
            account_methods.create_forums(i)
    # Clears the forum_list array so that the same forums aren't added to the array multiple times
    forum_list.clear()
    # Adds all forums in the database to an array and passes it to the account page
    forum_list = account_methods.add_forums_to_array(forum_list)
    posts_list = account_methods.get_posts_by_forum(0)
    example_posts_list = []
    if account_methods.get_last_discussion_ID() < 2:
        for i in range(3):
            example_posts_list.append(account_methods.generate_post(i))
    else:
        for i in range(3):
            example_posts_list.append(account_methods.get_post_by_ID(i + 1))


testing1 = tempUsername('Not Logged in')

@app.get('/')
def home():
    global example_posts_list
    if(testing1.getCurrentUsername == 'Not Logged in'):
        temp2 = testing1.getCurrentUsername()
        return render_template('homepage.html', example_posts_list = example_posts_list, currentUsername = temp2)
    else:
        temp2 = testing1.getCurrentUsername()
        return render_template('homepage.html', example_posts_list = example_posts_list, currentUsername = temp2)
    
#Define a route for the about page
@app.get('/about')
def about():
    return render_template('about.html',currentUsername = testing1.getCurrentUsername())
#Define a route for the features page
@app.get('/contact')
def contactUs():
    return render_template('contact.html',currentUsername = testing1.getCurrentUsername())

#Define a route for the homepage light mode
@app.route('/homepage-lightmode')
def homelight():
    return render_template('homepage-light-mode.html')
#Define a route for the create account page
@app.get('/account/new')
def signup():
    return render_template('signup.html', currentUsername = testing1.getCurrentUsername())

@app.get('/account/page')
def account():
    current_user = account_methods.get_account(testing1.getCurrentUsername())
    posts_list = account_methods.get_posts_by_user(testing1.getCurrentUsername())
    return render_template('account.html', account = current_user, forum_list = forum_list, posts_list = posts_list, currentUsername = testing1.getCurrentUsername())
#Takes input from create account page and refers to the users account page while also maintaining account
@app.post('/account')

def create_account():
    signupOrLogin = request.form.get('account_action')
    #----------------Signup Sheet if true----------------
    if (signupOrLogin == "signup"):
        accountExists = False
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        age = request.form.get('age')
        website = request.form.get('website')
        gender = request.form.get('gender')
        major = request.form.get('major')
        concentration = request.form.get('concentration')
        #This if statement below checks if the username already exists within the database
        
        #if(username == account_methods.get_account(username).username):
        if(username == ''):
            signupError = 'Account username cannot be nothing'
            return render_template('signup.html', error = signupError, currentUsername = testing1.getCurrentUsername())
        
        elif(account_methods.account_exists(username) == True):
            signupError = 'Account Name already exists please retry'
            return render_template('signup.html', error = signupError, currentUsername = testing1.getCurrentUsername())
        elif(account_methods.account_exists(username) != True):
            print("hello")
            created_account = account_methods.create_account(username, password, email, age, website, gender, major, concentration)
            #Changing global currentUsername variable
            account_methods.account_Authorization(username)
            testing1.setCurrentUsername(username)
            
            return redirect(f'/account/page')

    #----------------Login sheet if false----------------
    if (signupOrLogin == "login"):
        check_username = request.form.get('username')
        check_password = request.form.get('password')
        if(account_methods.account_exists(check_username) != True):
            loginError = 'Account does not exist1'
            return render_template('login.html', error = loginError, currentUsername = testing1.getCurrentUsername())
        
        elif (account_methods.verify_account(check_username, check_password) == True):
            login_account = account_methods.get_account(check_username)
            account_methods.account_Authorization(check_username)
        #Changing global currentUsername variable
            testing1.setCurrentUsername(check_username)     
            return redirect(f'/account/page')
        else:
            loginError = 'Password incorrect please retry'
            return render_template('login.html', error = loginError, currentUsername = testing1.getCurrentUsername())



#Define a route for the Login page
@app.get('/login')
def login():
    account_methods.account_deAuthorization(testing1.getCurrentUsername())
    testing1.setCurrentUsername('Not Logged in')
    return render_template('login.html', currentUsername = testing1.getCurrentUsername())
#Define a route for the each forum page
@app.get('/forum/<int:forum_id>')
def forum_page(forum_id):
    global current_forum_id
    sent_forum = account_methods.get_forum_by_id(forum_id)
    current_forum_id = forum_id
    posts_list = account_methods.get_posts_by_forum(forum_id)
    return render_template('forum_page.html', sent_forum = sent_forum, posts_list = posts_list, currentUsername = testing1.getCurrentUsername())
#recieve the value of the forum ID and redirect to that forum
@app.post('/forum')
def find_forum_page():

    forum_id = request.form.get('for_ID')

    print(forum_id)
    return redirect(f'/forum/{forum_id}')

#Define a route for the create post form
@app.get('/forum/create_post')
def create_forum_post():
    return render_template('create_forum_post.html', currentUsername = testing1.getCurrentUsername())
#Define a route for the each forum post
@app.get('/discussion/<int:discuss_ID>')
def show_discussion(discuss_ID):
    print("hello")
    reply_list = account_methods.get_replies_to_post(discuss_ID)
    show_post = account_methods.get_post_by_ID(discuss_ID)
    return render_template('discussion.html', show_post = show_post, reply_list = reply_list, currentUsername = testing1.getCurrentUsername())
#recieve the data from the create post form and redirect to the the discussion OR if the post already exist redirect to the post
@app.post('/discussion')
def post_discussion():
    first_posting = request.form.get('creating_post')
    global current_forum_id, current_user_id, discussion_counter
    if first_posting == "True":
        new_post_ID = int(account_methods.get_last_discussion_ID()) + 1
        creator_username = testing1.getCurrentUsername()
        parent_forum = current_forum_id
        parent_forum_name = account_methods.get_forum_by_id(current_forum_id).forum_name
        title = request.form.get('title')
        content = request.form.get('content')
        tags = request.form.get('tags')
        majors = request.form.get('majors')
        classes = request.form.get('classes')
        companies = request.form.get('companies')
        created_post = account_methods.create_post(new_post_ID, creator_username, parent_forum, parent_forum_name, title, content, tags, majors, classes, companies)

        return redirect(f'/discussion/{created_post.discuss_ID}')
    else:
        created_post = account_methods.get_post_by_ID(first_posting)
        return redirect(f'/discussion/{created_post.discuss_ID}')
    
@app.post('/comment')
def post_comment():
    first_posting = request.form.get('creating_post')
    reply_text = request.form.get('reply')
    reply_discuss_ID = int(first_posting)
    reply_ID = int(account_methods.get_last_reply_ID()) + 1
    reply_user = testing1.getCurrentUsername()
    new_reply = account_methods.create_reply(reply_ID, reply_text, reply_discuss_ID, reply_user)
    created_post = account_methods.get_post_by_ID(first_posting)
    return redirect(f'/discussion/{created_post.discuss_ID}')

# Define a route for user info
@app.get('/user-info')
def user_info():
    current_username = testing1.getCurrentUsername()
    if current_username != 'Not Logged in':
        # Retrieve the user information from the database based on the current session's username
        user = account_methods.get_account(current_username)
        return render_template('User_information.html', user=user, currentUsername=current_username)
    else:
        # Redirect to login page if the user is not logged in
        return redirect(url_for('login'))
    
# This is something Michael added for fun :)
@app.route('/sucks')
def sucksToSuck():
    return render_template('sucks.html', currentUsername = testing1.getCurrentUsername())

@app.get('/search/<string:search_data>')
def search(search_data):
    print(search_data)
    found_posts = account_methods.search_posts(search_data)
    return render_template('search.html', found_posts = found_posts, currentUsername = testing1.getCurrentUsername())

@app.post('/start_search')
def start_search():
    search_data = str(request.form.get('search_content'))
    return redirect(f'/search/{search_data}')

@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)



if __name__ == '__main__':
    app.run()
