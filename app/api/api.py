from fastapi import FastAPI
from sys import path
path.append('../')
from database.identify import IDENT
from os.path import dirname, abspath
from random import choices
from os import listdir



app = FastAPI()


class server():
    def __init__(self) -> None:
        pass

    @app.get('/getAUTH')
    def getKeys(account_code: str): #Use to choose a specific account, if any account be sent, return random 
        """
        Used to get api keys from youtube
        """

        return IDENT().return_data(identify_code=account_code)


    @app.get('/getVideo') #Require a video
    def getVideo(video_file: str = ''):
        """
        Used to get a video to upload, if no parameter is set, return a random video, otherwise
         return a selected video and return a error
        if these video doesn't exists
        """


        root_location = dirname(abspath("app")) #Get the root path
        if video_file:
            file_location = root_location + '/app/database/videos/' + video_file
            return file_location

        else:
            file_location = root_location + '/../database/videos/'
            videos = listdir(file_location)
            return choices(videos) #Return a random video
            






if __name__ == '__main__':
    server()