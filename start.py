"""
Main file, file whose manage everything
"""

from multiprocessing import Process
from app.database.crud import DB
from app.exceptions.database import UserAlreadyExists
    

def setting():
    """Create a file with location of webriver"""
    from app.vars.variable import LOCAL

    LOCAL().create_webdriver_location()


def server():
    """Run api server"""
    from app.api import api
    #Run api server
    api.run_api_server()


def tiktok(account_id: str, video: str = ''):
    """Upload video"""
    from app.tiktok import tiktok as TK

    if video:
        TK().run_tiktok_feature(account_id, video)
        #Run tiktok with video argument
    else:
        TK().run_tiktok_feature(account_id)
        #Run tiktok with no video argument

            

if __name__ == '__main__':
    from sys import argv
    from app.database.identify import IDENT

    database = DB() #Define database variable



    help_str = """
        Usage python3 start.py [option]
        
        -h or --help       Return commands

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
            database.returnAllUsers()
            
        elif arg == ('-cr' or '--createUser'):
            try:
                print(database.createUser(argv[2]))
            except UserAlreadyExists:
                print('[ERROR] The user already exists in database, the attempt to create duplicate user failed')


        elif argv[1] == 'run':
            """Run the entire code, server and tiktok"""
            print('Running Tikbot software...')

            user_status = database.checkUser(argv[2])
            #Check if user provided through command line exists, otherwise return a message in "else:"

            
            if user_status == True:
                #The uses exists
                #Run tiktok module and api module in paralell because both run together
            
                p2 = Process(target=tiktok, args=(argv[2]))
                p2.start()

                p1 = Process(target=server()) #Run server in paralell
                p1.start()

                p1.join()
                p2.join()
            else:
                print("[ERROR] Please provide a existent user id, to see all users type python3 start.py -u")

        else:
            print(help_str)
        
    except IndexError:
        print(help_str)

