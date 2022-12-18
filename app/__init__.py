from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os
#from management import User
import db
from countries import *
from process_aq import *
from db import *

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
<<<<<<< HEAD
setup()
=======
db.setup()
temp = list(db.populate_countries().values())
#temp_1 = list(db.get_final().values())
temp_1 = list(db.get_final().values())
>>>>>>> refs/remotes/origin/main

@app.route('/')
def index():
    if 'username' in session:
<<<<<<< HEAD
        temp = get_table_specifics("locationInfo","name")
        test = []
        for i in temp:
            test.append(i[0])
        return render_template('home_page.html',username = session['username'],air=test, dropdown=get_countries(), datastructure = get_final())
=======
        return redirect("/home")
>>>>>>> refs/remotes/origin/main
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
<<<<<<< HEAD
    '''
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    '''
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password')
        session['username'] = request.form['username']
        temp = get_table_specifics("locationInfo","name")
        test = []
        for i in temp:
            test.append(i[0])
        resp = render_template('home_page.html',username = session['username'],air=test, datastructure = get_final())
=======
    #Check if it already exists in database and render home page if it does
    #otherwise redirect to error page which will have a button linking to the login page
    username = request.form.get('username')
    password = request.form.get('password')
    if db.verify_account(username,password):
        session['username'] = username
        session['password'] = password
        return redirect("/home")
    if request.form.get('submit_button') is not None:
        return render_template("registration.html")
    else:
        resp = make_response(render_template('error.html',msg = "username or password is not correct"))
>>>>>>> refs/remotes/origin/main
        return resp

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        if db.add_account(userIn, passIn) == -1:
            return f"account with username {userIn} already exists"
        else:
            return render_template("register_success.html")
    return render_template("registration.html")

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect("/login")
    username = session['username']
    password = session['password']
    if db.verify_account(username, password):
        return render_template('home_page.html',username = session['username'],countriesinfo="TBD",countries=temp,locations=temp_1)

<<<<<<< HEAD
    # POST request: handle the form response and redirect
    username = request.form['username']
    password = request.form['password']
    if check_username(username) == True:
        return (make_response(render_template("error.html",msg="Username already exists, Please Login")))
    else:
        add_account(username,password)
        return redirect(url_for('login'))
=======
def verify_session():
    if 'username' in session and 'password' in session:
        if db.verify_account(session['username'], session['password']):
            return True
    return False
>>>>>>> refs/remotes/origin/main

@app.route('/direct_get_info',methods = ['GET', 'POST'])
def direct_get_info():
    if request.method == 'POST' and verify_session():
        loc = request.form.get('location')
        var = lookup_by_city_name(loc)
        if find_country_of(loc) != "Not Found":
            #return make_response(render_template("test.html",info=var,country_name=find_country_of(loc)))
            return make_response(render_template("direct.html",info=var,country_name=find_country_of(loc),selection=loc))
    return f"{loc}typed wrong"
    
        
@app.route('/find_locations', methods = ['GET', 'POST'])
def find_locations():
    if request.method == 'POST' and verify_session():
        country = request.form.get('name')
        country = db.convert(country)
        arr = get__all_cities(country)
        return make_response(render_template("locations.html",arr=arr))

@app.route('/extract_data', methods = ['GET', 'POST'])
def location_data():
    if request.method == 'POST' and verify_session():
        locations = request.form.get('location_name')
        dict_aq_data = lookup_by_city_name(locations)
        return make_response(render_template("measure.html",dict_aq_data=dict_aq_data))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
