"""
Main file, file whose manage everything
"""

from multiprocessing import Process
from app.database.crud import DB

    

def setting():
    """Create a file with location of webriver"""
    from app.vars.variable import LOCAL

    LOCAL().create_webdriver_location()


def server():
    """Run api server"""
    from app.api import api
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

    D = DB()



    help_str = """
        Usage python3 start.py [option]
        
        -h or --help       Return commands


        -i or --install:    Install dependencies and modules required to project, it's
         usually is used to the first use

         -s or --server:                 Run only the api server

         -t or --tiktok [account_id]:    Run exclusively tiktok module

         -c or --configure:              Configure settings

         -u or --users:                  Show all users 

        -cr or --createUser [username]   Create an user

         run [account code]              Run the entire program


        """
        
    try:
        arg = argv[1]

        if arg ==('-s' or '--server'):
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
            DB().returnAllUsers()
            
        elif arg == ('-cr' or '--createUser'):
            print(D.createUser(argv[2]))

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

