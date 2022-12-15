from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os
#from management import User
import db
from countries import *
from process_aq import *

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

user_header = ("(username TEXT, password TEXT)")
db.create_table("userInfo",user_header)
locations_header = ("(code TEXT, name TEXT)")
db.create_table("locationInfo",locations_header)
db.populate_countries()
#print(db.get_table_locs("locationInfo","locs"))

@app.route('/')
def index():
    if 'username' in session:
        return render_template('home_page.html',username = session['username'],countriesinfo="TBD",air="TBD")
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    '''
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password')
        session['username'] = request.form['username']
        resp = render_template('home_page.html',username = session['username'],countriesinfo="TBD",air="TBD")
        return resp
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if "username" in session:
        return redirect(url_for('index'))

    # GET request: display the form
    if request.method == "GET":
        return render_template("registration.html")

    # POST request: handle the form response and redirect
    username = request.form['username']
    password = request.form['password']
    if db.check_username(username) == True:
        return (make_response(render_template("error.html",msg="Username already exists, Please Login")))
    else:
        db.add_account(username,password)
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
