from fastapi import FastAPI

app = FastAPI()

class server():
    def __init__(self) -> None:
        pass

    @app.get('/getAUTH')
    def getKeys(account: str = 'OPTIONAL'): #Use to choose a specific account, if any account be sent, return random 
        """
        Used to get api keys from youtube
        """
        return 'API KEY to connection'

    @app.get('/getVideo')
    def getVideo(parameter: str = ''):
        """
        Used to get a video to upload, if no parameter is set, return a random video, otherwise
         return a selected video and return a error
        if these video doesn't exists
        """
        if not parameter:
            return 'Random video'

        return 'Some video'


if __name__ == '__main__':
    server()