from os.path import split, abspath, dirname
from yaml import load, FullLoader

def dbNAME():
    """Return Database name"""
    file_location, null = split(dirname(abspath(__file__)))

    file = open(file_location + '/vars/database.yaml')
    content_from_file = load(file, Loader=FullLoader)

    return content_from_file['DATABASE_NAME'] #Return database name
    
