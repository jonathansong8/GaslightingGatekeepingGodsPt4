from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os
#from management import User
import db
from countries import *
from process_aq import *
from test_weather_calls import *


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
db.setup()
temp = list(db.populate_countries().values())
#temp_1 = list(db.get_final().values())
temp_1 = list(db.get_final().values())
entry_countries = get_world_countries()
us_cities = get__all_cities("US")

@app.route('/')
def index():
    if 'username' in session:
        return redirect("/home")
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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
        resp = make_response(render_template('error.html',msg = "Username or Password is not correct"))
        return resp

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        if db.add_account(userIn, passIn) == -1:
            return render_template("error.html", msg = f"account with username {userIn} already exists")
        else:
            return redirect("/")
    return render_template("registration.html")

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect("/login")
    username = session['username']
    password = session['password']
    if db.verify_account(username, password):
        return render_template('home_page.html',username = session['username'],countries=temp,locations=temp_1,world=entry_countries,us_cities=us_cities)

def verify_session():
    if 'username' in session and 'password' in session:
        if db.verify_account(session['username'], session['password']):
            return True
    return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route('/direct_get_info',methods = ['GET', 'POST'])
def direct_get_info():
    if request.method == 'POST' and verify_session():
        loc = request.form.get('location')
        user_in = loc.split()
        if len(user_in)==2 and is_float(user_in[0]) and is_float(user_in[1]):
            try:
                curr = location(user_in[0],user_in[1])
            except:
                return render_template("error.html",msg=f"{loc} is not a valid location in the United States")
            try:
                info = forecast(user_in[0],user_in[1])
            except:
                return render_template("error.html",msg=f"Rate Limit Issue with Weather API. Please Try Again")
            return make_response(render_template("weather.html",info=info,country_name=curr[0],selection=curr[1]))   
        else:
            try:
                var = lookup_by_city_name(loc)
            except:
                return render_template("error.html",msg=f"{loc} is not a valid location")
            if find_country_of(loc) != "Not Found":
                #return make_response(render_template("test.html",info=var,country_name=find_country_of(loc)))
                return make_response(render_template("direct.html",info=var,country_name=find_country_of(loc),selection=loc))
    return redirect("/")
    
        
@app.route('/find_locations', methods = ['GET', 'POST'])
def find_locations():
    if request.method == 'POST' and verify_session():
        country = request.form.get('name')
        country_code = db.convert(country)
        if len(get__all_cities(country_code)) == 0:
            return render_template("error.html", msg = f"There are no cities available for {country} in the Air Quality API")
        else:
            arr = get__all_cities(country_code)
        return make_response(render_template("locations.html",arr=arr,username=session["username"]))
    return redirect("/")

@app.route('/extract_data', methods = ['GET', 'POST'])
def location_data():
    if request.method == 'POST' and verify_session():
        locations = request.form.get('location_name')
        rel_country = find_country_of(locations)
        dict_aq_data = lookup_by_city_name(locations)
        return make_response(render_template("measure.html",dict_aq_data=dict_aq_data,relevant=locations,rel_country=rel_country.capitalize()))
    return redirect("/")

@app.route('/countries_data', methods = ['GET', 'POST'])
def countries_data():
    if request.method == 'POST' and verify_session():
        country = request.form.get("country_name")
        try:
            country = get_country(country)
        except:
            country = "No data"
        return make_response(render_template("country.html", country=country))
    return redirect("/")

@app.route('/find_weather', methods = ['GET', 'POST'])
def find_weather():
    if request.method == 'POST' and verify_session():
        loc = request.form.get("location_name")
        try:
            loc_coords = lookup_city_coords(loc)
        except:
             return render_template("error.html",msg=f"No coordinates available for {loc}. Please Select An Alternate City")
        try:
            info = forecast(loc_coords[0],loc_coords[1])
        except:
            return render_template("error.html",msg=f"Rate Limit Issue with Weather API. Please Try Again")
        return make_response(render_template("weather_us.html", location=loc, country = "United States of America", info=info))
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
