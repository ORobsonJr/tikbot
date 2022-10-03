"""
This file will run the __main__.py file
"""
from os import system
from sys import version_info 

class setup():
    reQfile = 'requirements.txt'

    def __init__(self):
        self.python_version = version_info[0]
        

    def install(self):
        system('pip{py_v} install -r requirements.txt'.format(py_v=self.python_version)) #Install the requirements

        #Used to install prerequisites

    def server(self):
        system('cd app/api && uvicorn api:app --reload')


if __name__ == '__main__':
    from sys import argv

    SET = setup()

    try:
        if argv[1] ==('-i' or '--install'):
            SET.install()
        

        if argv[1] ==('-s' or '--server'):
            SET.server()
        
    except IndexError:
        print("""
        Usage python3 start.py [option]
        
        -i or --install:    Install dependencies and modules required to project, it's
         usually is used to the first use

         -s or --server:    Run only the api server

        """

        
        )
