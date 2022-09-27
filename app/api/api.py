from fastapi import FastAPI

app = FastAPI()

class server():
    def __init__(self) -> None:
        pass

    @app.get('/getAUTH')
    def getKeys(account: str = 'OPTIONAL'): #Use to choose a specific account, if any account be sent, return random 
        return 'API KEY to connection'

    @app.get('/getVideo')
    def getVideo(parameter: str = ''):
        if not parameter:
            return 'Random video'

        return 'Some video'


if __name__ == '__main__':
    server()