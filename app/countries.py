import requests

list_of_countries = '''Afghanistan
Albania
Algeria
Andorra
Angola
Antigua
Argentina
Armenia
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia
Botswana
Brazil
Brunei
Bulgaria
Burkina
Burundi
Cambodia
Cameroon
Canada
Cape Verde
Central African Rep
Chad
Chile
China
Colombia
Comoros
Congo
DRC
Costa Rica
Croatia
Cuba
Cyprus
Czech Republic
Denmark
Djibouti
Dominica
Dominican Republic
East Timor
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Fiji
Finland
France
Gabon
Gambia
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Ivory Coast
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
North Korea
South Korea
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
Norway
Oman
Pakistan
Palau
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Qatar
Romania
Russian Federation
Rwanda
Kitts
Lucia
Vincent
Samoa
San Marino
Sao Tome 
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Swaziland
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Togo
Tonga
Trinidad 
Tunisia
Turkey
Turkmenistan
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Uruguay
Uzbekistan
Vanuatu
Vatican City
Venezuela
Vietnam
Yemen
Zambia
Zimbabwe'''

table = []

def get_countries():
    for i in list_of_countries.split('\n'):
        API_URL = f"https://restcountries.com/v3.1/name/{i}"

        r = requests.get(API_URL) #creating a response object that will get us the information we needr
        api_dict = r.json() #r.json() returns a dictonary after deconding the response object
        population = (api_dict[0])["population"]
        capital = (api_dict[0])["capital"]
        for j in capital:
            capital = j
        flag = (api_dict[0])["flag"]
        
        table.append((i, str("Population of " + i + ": " + str(population)), capital, flag))
    
    new = ""
    for i in table:
        new = new + ""
        for j in range(len(i)):
            if (j < len(i)-1):
                new = new + str(i[j]) + ", "
            else:
                new = new + str(i[j])
        new = new + "</a>\n"
    return new


def get_country(country_name):
    API_URL = f"https://restcountries.com/v3.1/name/{country_name}"

    r = requests.get(API_URL) #creating a response object that will get us the information we needr
    api_dict = r.json() #r.json() returns a dictonary after deconding the response object
    population = (api_dict[0])["population"]
    capital = (api_dict[0])["capital"]
    for j in capital:
        capital = j
    flag = (api_dict[0])["flag"]
    new = "<strong>Country</strong>: " + country_name + "<br> \n <strong>Population</strong>: " + str(population) + "<br> \n <strong>Capital</strong>: " + capital + "<br> \n <strong>Flag</strong>: " + flag
    return new
    

