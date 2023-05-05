from flask import Flask, abort, redirect, render_template, request, send_from_directory
from src.repositories.methods import account_methods
from src.models import db

app = Flask(__name__, template_folder='templates', static_folder='StaticFile')
#Change password below to your own SQL Database Password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CHANGE PASSWORD HERE @localhost:3306/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
if_Create_Account = False
forum_list = []
#Define a route for the homepage
@app.get('/')
def home():
    
#------------!!!-uncomment line below and run app.py to clear the database-!!!------------
    #account_methods.clear_data()
#-----------------------------------------------------------------------------------------    
    account_methods.create_data()
    return render_template('homepage.html')

#Define a route for the about page
@app.get('/about')
def about():
    return render_template('about.html')
#Define a route for the features page
@app.get('/features')
def features():
    return render_template('features.html')

#Define a route for the homepage light mode
@app.route('/homepage-lightmode')
def homelight():
    return render_template('homepage-light-mode.html')
#Define a route for the create account page
@app.get('/account/new')
def signup():
    return render_template('signup.html')
#Define a route for the user's account page
@app.get('/account/<string:username>')
def account(username):
    current_user = account_methods.get_account(username)
    global forum_list
    # if there are no forums in the database, create them
    if account_methods.get_number_of_forums() == 0:
        for i in range(3):
            account_methods.create_forums(i)
    # Clears the forum_list array so that the same forums aren't added to the array multiple times
    forum_list.clear()
    # Adds all forums in the database to an array and passes it to the account page
    forum_list = account_methods.add_forums_to_array(forum_list)
    return render_template('account.html', account = current_user, forum_list = forum_list)
#Takes input from create account page and refers to the users account page
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
        if(account_methods.account_exists(username) == True):
            error = 'Account Name already exists please retry'
            return render_template('signup.html', error2 = error)
        elif(account_methods.account_exists(username) != True):
            created_account = account_methods.create_account(username, password, email, age, website, gender, major, concentration)
            #return render_template('account.html', )
            return redirect(f'/account/{created_account.username}')

    #----------------Login sheet if false----------------
    if (signupOrLogin == "login"):
        check_username = request.form.get('username')
        check_password = request.form.get('password')

        check_account = account_methods.verify_account(check_username, check_password)
    if (check_account == True):
        created_account = account_methods.get_account(check_username)
        return redirect(f'/account/{created_account.username}')


#Define a route for the Login page
@app.get('/login')
def login():
    return render_template('login.html')
@app.get('/forum/<int:forum_id>')
def forum_page(forum_id):
    sent_forum = account_methods.get_forum_by_id(forum_id)
    return render_template('forum_page.html', sent_forum = sent_forum)
@app.post('/forum')
def find_forum_page():
    forum_id = request.form.get('for_ID')
    print(forum_id)
    return redirect(f'/forum/{forum_id}')
    
@app.get('/forum/create_post')
def create_forum_post():
    return render_template('create_forum_post.html')

#app.get('discussion//<string:title>')
#def show_discussion():
    #return render_template()
@app.post('/discussion')
def post_discussion():
    return redirect(f'/discussion/{}')
#Send images


@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)

if __name__ == '__main__':
    app.run()
