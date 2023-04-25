from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='StaticFile')

#Define a route for the homepage
@app.route('/')
def home():
    return render_template('homepage.html')

#Define a route for the about page
@app.route('/about')
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

#Define a route for the account page
@app.route('/account')
def account():
    return render_template('account.html')

#Send images
@app.route('/Images/<path:path>')
def send_image(path):
    return send_from_directory('Images', path)

if __name__ == '__main__':
    app.run()