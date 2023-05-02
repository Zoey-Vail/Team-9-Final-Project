from flask import Flask, abort, redirect, render_template, request, send_from_directory
from src.repositories.methods import account_methods
from src.models import db


app = Flask(__name__, template_folder='templates', static_folder='StaticFile')
#DO NOT FORGET TO CHANGE THE PASSWORD BELOW TO THE ONE WITHIN YOUR MYSQL WORKBENCH THIS IS DIFFERENT FOR EVERYONE
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mikerocks2319!@localhost:3306/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if_Create_Account = False

#Define a route for the homepage
@app.get('/')
def home():
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
    return render_template('account.html', account = current_user)

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
        else:
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



#Send images
@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)

if __name__ == '__main__':
    app.run()

