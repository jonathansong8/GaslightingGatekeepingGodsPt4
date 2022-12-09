# ArRESTed Development by GaslightingGatekeepingGodsPt4
# Jonathan Song, Daniel Liu, Nicholas Tarsis, Kevin Xiao
# Description

The API’s we will use are the Google Maps API, Air Quality API, Water Quality API, and to some extent, the Country API. We will use the Google Maps API to create tables of relevant data. Once the user clicks on a country, a window will pop up in the corner of their screen for that country that displays relevant information specific to that country, like Air Quality and Water Quality. In order to fully customize the window, we will use the Country API to show data like flags and population.

# Launch Codes
0. Clone repository

 ```bash
 git clone git@github.com:jonathansong8/GaslightingGatekeepingGodsPt4.git
 ```

1. `cd` into the local repository

 ```bash
 cd P00-Move-Slowly-and-Fix-Things
 ```

2. Install necessary packages

 ```bash
 pip install -r requirements.txt
 ```
3. `cd` into the app directory

 ```bash
 cd app
 ```
4. Start Flask server

 ```bash
 python app/__init__.py
 ```

5. Visit `http://127.0.0.1:5000/` in browser

