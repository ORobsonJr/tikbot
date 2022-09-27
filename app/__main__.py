

"""
It's the setup file where user will run the whole program and your funcionalities
"""

from multiprocessing import Process
from os import system

def server():
    from os import system

    try:
        system('cd api && uvicorn api:app --reload')
        print('[*] Server started sucessfully')

    except Exception as error_api:
        print('A error trying run api server occurred: ', error_api)




if __name__ == '__main__':
    "Run the instances in paralell"
    p1 = Process(target=server)
    #
