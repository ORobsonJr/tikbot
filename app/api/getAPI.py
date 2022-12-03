from app.vars.variable import LOCAL
from requests.exceptions import ConnectionError
from requests import post, get, put


  
class handleAPI():
    def __init__(self):
        self.url = LOCAL().url()
        self.getAUTH_ = self.url + 'getAUTH'
        self.getVideo_ = self.url + 'getVideo'
        self.postCookies_ = self.url + 'postCookies'


        

    def getAUTH(self, id_account: str):
        """
        Get the parameters to login, including cookies and others...
        """
        try: #If value was sended, return...
            att = get(
                url=self.getAUTH_,
                params={'account_code':id_account}
                )

            return att.json()
                

        except ConnectionError:
            raise ConnectionError('[YOUTUBE] ERROR in getAPI, check if api server still on')

    def getVideo(self, video: str = ''):
        """
        Get the video to be posted by API

        """
        try:
            if video:
                att = get(url=self.getVideo_,
                params={'video_file':video}
                )

                decode = att.content.decode('utf-8')
                return eval(decode) #If video was provided, we return a specific 

            else:
                att = get(url=self.getVideo_)

                decode = att.content.decode('utf-8')
                return eval(decode)
        

        except ConnectionError:
            print('[YOUTUBE] Connection error, check if api server is on')



    def putCookies(self, account_code: str, cookies: list):
        cookies = str(cookies).replace("'", '"') #Replace all ' because is not compatible in .json files
        cookies = list(cookies)

        """
        In the end of operation you post your cookies to keep everything well update

        It's very useful especially to cookies, that is what we're uploading in the case 
        """
        try:
            attempt = put(self.postCookies_, params={'account_code': account_code}, json=cookies)
            print('Sending cookies to server in {url}...'.format(url=self.postCookies_))
            #print('Response: ',attempt.content, attempt.status_code)

            if  attempt.status_code == 200:
                return {'STATUS': 200, 'DATA': attempt.content.decode('utf-8')}

            return print('[YOUTUBE] Error while upload cookies to api server')

        except ConnectionError:
            print('[YOUTUBE] Connection error, check if api server is on')




