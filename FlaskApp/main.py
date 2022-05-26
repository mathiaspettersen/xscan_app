import sqlite3
from flask import Flask, render_template, session, Blueprint, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_sqlalchemy import SQLAlchemy
#from .models import User
#from . import db


# Killing the process to prevent database lock
'''
try:
        os.system('fuser -k main.py')
except:
        pass
'''
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '12345678'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


app = Flask(__name__)

@app.route('/')
def main():
	
	
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template('about.html')



@app.route('/profile', methods=["GET", "POST"])
def profile():
	if request.method == "POST":
		ip_addr = request.form.get("ip_address")
		ip_scanner = os.system(("nmap -T4 -A -p0-100 -oN ip_user_output.txt {}".format(ip_addr)))

		return redirect(url_for('results_scan'))
	
	return render_template('profile.html')

@app.route('/results', methods=["GET", "POST"])
def results_scan():
	os.system("sed '/^$/d' ip_user_output.txt && sed -i '1,4d' ip_user_output.txt && sed -i '$d' ip_user_output.txt && sed -i '$d' ip_user_output.txt")

	with open("ip_user_output.txt", "r") as f:
		
		return render_template('results.html', text=f.read())

'''
Authentication
'''

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('app.login'))  

@app.route('/logout')
def logout():
    return 'Logout'