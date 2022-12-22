from app.api.getAPI import handleAPI
from app.tiktok.config import selenium_connection as sh



driver = sh.driver

class configure():
    
    def __init__(self, account_id: str):
        self.HG = handleAPI() #Make requests to api
        self.AUTH_ = self.HG.getAUTH(id_account=account_id) #Get the parameters to authenticate using cookies
        self.account_id = account_id  #Account id


    def use_cookies(self, cookies_: list):
        """
        Load cookies in the browser
        """
        try:
            for c in cookies_:
                print(c)
                driver.add_cookie(c)
        except TypeError:
            pass

    def get_cookies(self):
        """Get cookies of current session"""
        return driver.get_cookies()

    def post_cookies(self, cookies_: list):
        """
        Post cookies of session to api server
        """
        attempt = self.HG.postCookies(account_code=self.account_id, cookies=cookies_)
        return attempt