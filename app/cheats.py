import sqlite3

DB_FILE = "zetten.db"

def execute(command):

    with sqlite3.connect(DB_FILE) as db:

            c = db.cursor()
            result = c.execute(command)
            db.commit()
    
    return result

def setup():
    
    execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id           INTEGER PRIMARY KEY,
            username     TEXT,
            password     TEXT
        )
        '''
                
    )
