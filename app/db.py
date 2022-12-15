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

def add_info(code, name):
    query("INSERT INTO locationInfo VALUES (?, ?)", (code, name))


all_countries = process("https://api.openaq.org/v2/countries?limit=200&page=1&offset=0&sort=asc&order_by=country")
dict_countries = {}
for country in all_countries:
    code = country["code"]
    name = country["name"]
    dict_countries[code] = name

locations_header = ("(code TEXT, name TEXT)")
create_table("locationInfo",locations_header)
for x,y in dict_countries.items():
    print(x)
    print(y)
    add_info(x,y)
