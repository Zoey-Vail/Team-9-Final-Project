from flask import Flask, abort, redirect, render_template, request, send_from_directory
from src.repositories.methods import account_methods
from src.models import db

# TODO: DB connection

app = Flask(__name__, template_folder='templates', static_folder='StaticFile')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:32011509@localhost:3306/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


#Define a route for the homepage
@app.route('/')
def home():
    account_methods.create_data()
    return render_template('homepage.html')

#Define a route for the about page
@app.get('/about')
def about():
    return render_template('about.html')

#Define a route for the homepage light mode
@app.route('/homepage-lightmode')
def homelight():
    return render_template('homepage-light-mode.html')

#Define a route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.get('/signup')
def account():
    return render_template('signup.html')
@app.get('/account<string:username>')
def account_page(username):
    return render_template('login.html')
@app.post('/account')
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    age = request.form.get('age')
    website = request.form.get('website')
    gender = request.form.get('gender')
    major = request.form.get('major')
    concentration = request.form.get('concentration')
    created_account = account_methods.create_account(username, password, email, age, website, gender, major, concentration)
    return render_template('account.html', created_account = created_account)

#Define a route for the account page

#Send images
@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)

if __name__ == '__main__':
    app.run()