from fastapi import FastAPI
from sys import path
path.append('../')
from database.reader import FETCH as AUTH
from fastapi import HTTPException


app = FastAPI()
id = AUTH.id #Define id from csv file
token = AUTH.token #Define token from csv file


class server():
    def __init__(self) -> None:
        pass

    @app.get('/getAUTH')
    def getKeys(): #Use to choose a specific account, if any account be sent, return random 
        """
        Used to get api keys from youtube
        """

        try:
            return {'STATUS': 200, 'id': id, 'token': token}
        except:
            return {'STATUS': 500}


    @app.get('/getVideo') #Require a video
    def getVideo(parameter: str = ''):
        """
        Used to get a video to upload, if no parameter is set, return a random video, otherwise
         return a selected video and return a error
        if these video doesn't exists
        """
        if not parameter:
            return 'Random video'

        return 'Some video'


    @app.get('/getProfile') #Get the profile fingerprint
    def getProfile(account: str = ''):
        if account:
            return {
            'canvas': ''
            }

        if not account: #Return a random profile
            return {
                'canvas': 'random'
            }


if __name__ == '__main__':
    server()