import sqlite3
from process_aq import *

DB_FILE = "zetten.db"

def query(sql, extra = None):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    if extra is None:
        res = c.execute(sql)
    else:
        res = c.execute(sql, extra)
    db.commit()
    db.close()
    return res

def create_table(name, header):
    query(f"CREATE TABLE IF NOT EXISTS {name} {header}")

def add_account(username, password):
    if not(check_username(username)):
        query("INSERT INTO userInfo VALUES (?, ?)", (username, password))
    else:
        return -1

def check_username(username):
    accounts = get_table_contents("userInfo")
    for account in accounts:
        if account[0] == username:
            return True
    return False
#return true if username and password are in db, false if one isn't
def verify_account(username, password):
    accounts = get_table_contents("userInfo")
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

def get_table_contents(tableName):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT * from {tableName}")
    out = res.fetchall()
    db.commit()
    db.close()
    return out

'''
def get_table_specifics(tableName, search):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT {search} from {tableName}")
    out = res.fetchall()
    db.commit()
    db.close()
    return out


def add_info(code, name):
    query("INSERT INTO locationInfo VALUES (?, ?)", (code, name))
'''

def populate_countries():
    all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
    dict_countries = {}
    for country in all_countries:
        code = country["code"]
        name = country["name"]
        dict_countries[code] = name
    return dict_countries

def setup():
    user_header = ("(username TEXT, password TEXT)")
    create_table("userInfo",user_header)

def get_final():
    all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
    temp_dict = {}
    for country in all_countries:
        code = country["code"]
        name = country["name"]
        all_locs = get__all_cities(code)
        temp_dict[name] = all_locs
    return temp_dict
<<<<<<< HEAD
=======

def convert(name):
    all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
    for country in all_countries:
        if country["name"] == name:
            return country["code"]
>>>>>>> refs/remotes/origin/main
