from app.vars import database
from sys import path
from os.path import dirname,abspath,split, exists

"""
Checks if there is a local database in the folder, if not, create and configure it
"""

path.append('.')
__all__ = ['database']


#Configure Database if doesn't exists
rdir, none = split(dirname(abspath(__file__)))
directory = rdir + '/database/' + database.dbNAME() #Database file location
DBexistence = exists(directory)

if DBexistence == False:
    """If Database does't exists, create and configure"""
    from app.database import setup
    setup.create()
