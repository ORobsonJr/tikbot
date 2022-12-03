from fastapi import FastAPI, HTTPException
from os.path import dirname, abspath
from random import choices
from sys import path
path.append('../../')
from app.database.identify import IDENT
from os.path import exists
from app.vars.variable import LOCAL
from uvicorn import run

app = FastAPI()
L = LOCAL()



class server():
    def __init__(self):
        self.L = LOCAL() 
        

    @app.get('/getAUTH')
    def getKeys(account_code: str): #Use to choose a specific account, if any account be sent, return random 
        """
        Return parameters to login, in this case cookies.
        """
        try:
            account_code = account_code.replace(' ', '') #Sometimes we receive account_code with space, then let's replace it to avoid conflicts

            file = IDENT(account_code).return_data()
            if file:
                arg = file['cookies']

                if type(arg) == str: #Sometimes the file is stored in string format
                    return eval(arg)

                return file['cookies']
            else:
                raise HTTPException(status_code=404, detail='NOT FOUND')

        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail='NOT FOUND '+e)
            

    @app.get('/getVideo') #Require a video
    def getVideo(video_file: str = ''):
        """
        Used to get a video to upload, if no parameter is sended, return a random video.
        Raise exception if these video doesn't exists.
        """

        try:
            if video_file:
                return L.return_video(video_file)
            return L.return_video() #Random
        except FileNotFoundError:
            raise HTTPException(
                status_code=404,
                detail='EMPTY PATH'
            )


    @app.put('/putCookies')
    def putCookies(cookies: dict, account_code: str):
        """Update cookies of a specific account"""

        try:
            IDENT(account_code).update_data(value=cookies)

            return 

        except FileNotFoundError:
            raise HTTPException(
                status_code=400,
                detail=f'FileNotFoundError',
                )

    


def __main__():
    run(app, host='localhost', port=8000)
