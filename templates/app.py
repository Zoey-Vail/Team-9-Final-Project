from flask import Flask, abort, redirect, render_template, request, send_from_directory
from src.repositories.methods import account_methods
from src.models import db


app = Flask(__name__, template_folder='templates', static_folder='StaticFile')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:32011509@localhost:3306/accounts'
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
    exists = request.form.get('if_exists')
    if (exists == "True"):
        print('true')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        age = request.form.get('age')
        website = request.form.get('website')
        gender = request.form.get('gender')
        major = request.form.get('major')
        concentration = request.form.get('concentration')
        created_account = account_methods.create_account(username, password, email, age, website, gender, major, concentration)
    if (exists == "False"):
        print('false')
        check_username = request.form.get('username')
        check_password = request.form.get('password')
        created_account = account_methods.verify_account(check_username, check_password)
    return redirect(f'/account/{created_account.username}')
#Define a route for the Login page
@app.get('/login')
def login():
    return render_template('login.html')

#Define a route for the account page

#Send images


@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)

if __name__ == '__main__':
    app.run()