from sys import path
from os.path import dirname, abspath
root_location = dirname(abspath("app")) + '/app/vars'
path.append(root_location)
from variable import LOCAL

from requests.exceptions import ConnectionError
from requests import post, get



class handleAPI():
    def __init__(self):
        self.url = LOCAL().url()
        

    def getAUTH(self, value: str):
        route = self.url + 'getAUTH' 
        try:
            attempt = get(route, params={'account_code': value})
            if attempt.status_code == 200:
                return attempt.json()

            return {'STATUS': 'ERROR', 'LOCATION': "youtube"}

        except ConnectionError:
            print('Connection error, check if api server is on')

    def getVideo(self, video: str = 'NONE'):
        route = self.url + 'getVideo'
        try:
            attempt = get(route, params={'account_code': value})
            return attempt.json()

        except ConnectionError:
            print('Connection error, check if api server is on')


print(handleAPI().getAUTH(value='1'))
