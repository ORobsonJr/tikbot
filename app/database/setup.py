
"""
Setup the database
"""

import sqlite3 as sql
from os.path import split, abspath, dirname
from app.vars import database 

def create():
    #Create
    app_path, file = split(dirname(abspath(__file__)))
    db_name = app_path + '/database/' + database.dbNAME()
    #Location of DB

    con = sql.connect(db_name)

    #Configure
    createDB = """
    CREATE TABLE ACCOUNTS (
        ACCOUNT_ID INTERGER PRIMAR KEY,
        ACCOUNT_NAME TEXT PRIMAR KEY,
        COOKIES ARRAY
        );
    """
    
    cr = con.cursor()
    
    cr.execute(createDB) #Configure tables

