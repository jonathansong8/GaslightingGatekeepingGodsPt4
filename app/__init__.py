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
db.setup()
temp = list(db.populate_countries().values())
#temp_1 = list(db.get_final().values())
temp_1 = list(db.get_final().values())

@app.route('/')
def index():
    if 'username' in session:
        return render_template('home_page.html',username = session['username'],countriesinfo="TBD",air="TBD", dropdown = get_countries())
        temp = db.get_table_specifics("locationInfo","name")
        test = []
        for i in temp:
            test.append(i[0])
        return render_template('home_page.html',username = session['username'],air=test)
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
        resp = render_template('home_page.html',username = session['username'],countriesinfo="TBD",air="TBD", dropdown = get_countries())
        temp = db.get_table_specifics("locationInfo","name")
        test = []
        for i in temp:
            test.append(i[0])
        resp = render_template('home_page.html',username = session['username'],air=test)
        return resp

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        if db.add_account(userIn, passIn) == -1:
            return render_template("error.html", msg = f"account with username {userIn} already exists")
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

    # POST request: handle the form response and redirect
    username = request.form['username']
    password = request.form['password']
    if db.check_username(username) == True:
        return (make_response(render_template("error.html",msg="Username already exists, Please Login")))
    else:
        db.add_account(username,password)=="TBD", dropdown == "TBD"
        return render_template('login.html')
    db.add_account(username,password)
    return redirect(url_for('login'))

@app.route('/direct_get_info',methods = ['GET', 'POST'])
def direct_get_info():
    if request.method == 'POST' and verify_session():
        loc = request.form.get('location')
        var = lookup_by_city_name(loc)
        if find_country_of(loc) != "Not Found":
            #return make_response(render_template("test.html",info=var,country_name=find_country_of(loc)))
            return make_response(render_template("direct.html",info=var,country_name=find_country_of(loc),selection=loc))
    return render_template("error.html",msg=f"{loc}typed wrong")
    
        
@app.route('/find_locations', methods = ['GET', 'POST'])
def find_locations():
    if request.method == 'POST' and verify_session():
        country = request.form.get('name')
        country = db.convert(country)
        arr = get__all_cities(country)
        try:
            arr2 = get_country(country)
        except:
            arr2 = " pls work"
        return make_response(render_template("locations.html",arr=arr, arr2=arr2))
 'POST' and verify_session():
        country = request.form.get("country_name")
        print(country)
        try:
            country = get_country(country)
        except:
            country = "No data"
        return make_response(render_template("country.html", country=country))
 'POST' and verify_session():
        locations = request.form.get('location_name')
        dict_aq_data = lookup_by_city_name(locations)
        try:
            country = request.form.get("country_data")
        except:
            country = " THERE WAS NO COUNTRY??"
        return make_response(render_template("measure.html",dict_aq_data=dict_aq_data,country=country))

@app.route('/countries_data', methods = ['GET', 'POST'])
def countries_data():
    if request.method == 'POST' and verify_session():
        country = request.form.get("country_name")
        print(country)
        try:
            country = get_country(country)
        except:
            country = "No data"
        return make_response(render_template("country.html", country=country))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
