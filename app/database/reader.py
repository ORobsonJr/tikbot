from csv import reader
from sys import path 
path.append('../')
#from vars import *

def current_time():
    from datetime import datetime

    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


def read_CSV(file, mode:bool = None):
    with open(file, 'r') as f:
        """
        Read the csv file where is stored the token
        """
        if mode == None:
            rows = reader(f, delimiter=",", lineterminator="\n")
            auth = {'code_account': '', 'id': '', 'token': '', 'last_use': ''}
            for c in rows:
                if c[1] == 'ON' or 'on': #It's avaliable
                    auth['id'] = c[1]
                    auth['hash'] = c[2]
                    auth['code_account'] = c[3]
                    auth['last_use'] = c[4]


            if (auth['id'] =='id') or (auth['token'] =='token'):
                auth = {'STATUS': 'SOME PROBLEM HAPPEN'}


                return auth

            return auth #Return login parameters

        return f.read()

get_location = __file__[]
file_name = 'logs_authentication.csv'
login_parameters = read_CSV(file=file_name)

class FETCH():
    id = login_parameters['id']
    token = login_parameters['token']
    code_account = login_parameters['code_account']

    def __init__(self) -> None:
        pass
    
    def change_status(self, identifier: str):
        content = read_CSV(file=file_name, mode=True) #Get the content to edit

        

        #edit


