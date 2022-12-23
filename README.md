# ArRESTed Development by GaslightingGatekeepingGodsPt4
# Jonathan Song, Daniel Liu, Nicholas Tarsis, Kevin Xiao
# Description

The APIs we used are: Air Quality API, Country API, and the Weather API. Once the user clicks on a country from a dropdown, they will be redirected to different pages, depending on whether they are looking for country or air quality data (which are different dropdowns in different sections). On the countries page, data will be displayed like population, capital, currency, time zone, latitude/longitude, language, map link, and flag image. On the home page, there is a search bar where one can enter the city name to directly search up air quality values. On the air quality page, air quality values will be organized in a tabular format. Furthermore, one can enter latitude and longitude values within the search bar, seperated by only a space, which will be parsed and matched to that location (currently only in the US) to display the forecast for the day. 
Some Sample Values are: (35,-78) (45 -90) (42 -71)
Site of US States Laitiude/Longitude Values: https://www.latlong.net/category/states-236-14.html

# Relevant API Cards

Air Quality API: https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_air_quality.md \
Country API: https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_countries.md \
Weather API: https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_weatherAPI.md

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
 cd app/
 ```
4. Start Flask server

 ```bash
 python __init__.py
 ```

5. Visit `http://127.0.0.1:5000/` in browser

