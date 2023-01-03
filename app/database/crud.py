from os.path import dirname, abspath, exists, split
from sys import path
path.append('.')
from json import load as read
from json import dump as write
import sqlite3
from app.exceptions.database import UserAlreadyExists
from app.vars import database


class DB():
    """
    Return values required in sqlite database
    """

    def __init__(self):
        self.cookies = 'cookies'
        self.account_name = ''

        rdir, none = split(dirname(abspath(__file__)))
        directory = rdir + '/database/' + database.dbNAME() #Database file location
        self.conn = sqlite3.connect(directory) #Object to connect
        self.csor = self.conn.cursor() #Cursor

    def return_data(self, user_id):
        """
        Return data
        """

        self.csor.execute(f"SELECT * FROM ACCOUNTS WHERE ACCOUNT_ID = {user_id}")
        values = self.csor.fetchone()
        if values:
            account_id_, account_name_, cookies_ = values[0], values[1], values[2]

            return {
            "account_id": account_id_, 
            "account_name": account_name_,
            "cookies": cookies_
            }
   
        return


    def update_data(self,user_id: str, value: dict = {}, account_name_: str = ''):
        """
        Update data in DB
        """

        if value: SQL = f"UPDATE ACCOUNTS SET COOKIES WHERE ACCOUNT_ID = '{user_id}'" #Update cookies
        elif account_name_: SQL = f"UPDATE ACCOUNTS SET COOKIES WHERE ACCOUNT_NAME = '{account_name_}'" #Update cookies

        self.csor.execute(SQL)
        self.conn.commit()


        

    def checkUser(self, account_code: str = '', account_name: str = ''):
        """Check the existence of some user"""
        if account_code:
            SQL = f"SELECT * FROM ACCOUNTS WHERE  ACCOUNT_ID = '{account_code}'"

        else:
            SQL = f"SELECT * FROM ACCOUNTS WHERE  ACCOUNT_NAME = '{account_name}'"

        self.csor.execute(SQL)
        user_ = self.csor.fetchone()
        #If user founded
        if user_:
            return True #Return True

        return False #Doesn't exists
        
        

    def createUser(self, username: str):
        """Create an user in Database"""

        count_users = self.csor.execute('SELECT * FROM ACCOUNTS')
        count_users = len(self.csor.fetchall())

        verify_user_existence = DB().checkUser(account_name=username)

        if verify_user_existence == False:
            SQL = f"INSERT INTO ACCOUNTS (ACCOUNT_ID, ACCOUNT_NAME) VALUES ('{str(count_users+1)}', '{username}');"
            self.csor.execute(SQL)
            self.conn.commit()
            return 'User created sucessfully'
        
        raise UserAlreadyExists(username)

    def removeUser(self, user):
        """Remove user from DB"""

        SQL = f"REMOVE FROM ACCOUNTS WHERE ACCOUNT_ID = '{user}'"
        self.csor.execute(SQL)
        self.conn.commit()

    def returnAllUsers(self):
        """Return all users from DataBase"""
        SQL = "SELECT * FROM ACCOUNTS;"
        self.csor.execute(SQL)
        all_users = self.csor.fetchall()
        print('Avaliable accounts\nID   ACCOUNT NAME')
        for u in all_users:
            print('[{id}] - {account_name}'.format(id=u[0], account_name=u[1]))

