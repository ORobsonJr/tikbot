"""
Main file, file whose manage everything
"""

from os import system
from sys import version_info 
from multiprocessing import Process
from app.vars.variable import LOCAL
from app.api import api


reQfile = 'requirements.txt'

python_version = version_info[0] #Python version
    
def install():
    """Install requirements.txt using the current version of python"""
    system('pip{py_v} install -r {file}'.format(py_v=python_version, file=reQfile)) #Install the requirements
    system(f'python{python_version} setup.py install')

def setting():
    """Create a file with location of webriver"""
    from app.vars.variable import LOCAL

    LOCAL().create_webdriver_location()


def server():
    """Run api server"""
    api.__main__()


def tiktok(account_id: str, video: str = ''):
    """Upload video"""
    from app.tiktok.start import TIKTOK as TK

    if video:
        TK().__main__(account_id, video)
    else:
        TK().__main__(account_id)


            

if __name__ == '__main__':
    from sys import argv
    from app.database.identify import IDENT


    help_str = """
        Usage python3 start.py [option]
        
        -h or --help       Return commands


        -i or --install:    Install dependencies and modules required to project, it's
         usually is used to the first use

         -s or --server:    Run only the api server

         -t or --tiktok [account_id]:    Run exclusively tiktok module

         -c or --configure:    Configure settings

         -u or --users:    Show all users 

         run [account code]               Run the entire program


        """
        

    L = LOCAL()

    try:
        arg = argv[1]

        if arg ==('-i' or '--install'):
            print('Installing...')
            install()
        

        elif arg ==('-s' or '--server'):
            print('Running exclusively api server...')
            server()

        elif arg ==('-t' or '--tiktok'):
            print('Running exclusively tiktok module')
            tiktok(argv[2])

        elif arg == ('-h' or '--help'):
            print(help_str)

        elif arg == ('-c' or '--configure'):            
            setting()

        elif arg == ('-u' or '--users'):
            try:
                account_argument = argv[2]
                LOCAL(account_argument).return_users()
            except IndexError:
                LOCAL().return_users()

        elif argv[1] == 'run':
            """Run the entire code, server and tiktok"""
            print('Running Tikbot software...')

            user_status = IDENT(account_id=argv[2]).checkUser()

            
            if user_status == True:
            
                p2 = Process(target=tiktok, args=(argv[2]))
                p2.start()

                p1 = Process(target=server()) #Run server in paralell
                p1.start()

                p1.join()
                p2.join()
            else:
                print("Please provide a existent user id, to see all users type python3 start.py -u")

        else:
            print(help_str)
        
    except IndexError:
        print(help_str)

