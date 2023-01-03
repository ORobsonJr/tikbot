from app.tiktok.config import selenium_connection as sh
from app.api.getAPI import handleAPI
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from app.vars import var_tiktok as TK
from app.tiktok.config.settings import configure



"""
Upload video to tiktok"""

driver = sh.driver #Import selenium connection




class UPLOAD():
    def __init__(self, account_id: str, title: str = ''):
        self.HG = handleAPI() #Make requests to api
        self.AUTH_ = self.HG.getAUTH(id_account=account_id) #Get the parameters to identify 
        self.account_id = account_id  #Define account id
        self.C = configure(account_id=self.account_id)

        #Video parameters
        self.title_ = title


        #Routes
        self.root_url = TK.root_route() 
        self.upload_url = TK.upload_route() #Link to upload

    def __main__(self, video: str = ''):
        """
        Main def
        """
        if not video:
            #choose a random video
            VIDEO_PATH = self.HG.getVideo()
            #Define video localization, in this case as no argument was provided, we'll receive a random video
        else:
            VIDEO_PATH = self.HG.getVideo(video)
            #Return a video location, if video doesn't exists raise a FileNotFoundError


        try:
            print('Loading tiktok...') 
            driver.get(self.root_url) #Open tiktok link
            print('Tiktok opened')
            

            """
            Load cookies
            """
            
            try:
                self.C.use_cookies(cookies_=self.AUTH_) #Load cookies
                driver.refresh() #Refresh the current page
                sleep(3)

            except InvalidCookieDomainException:
                """
                The domain provided in cookies by api is inchoerent to current address, for seecurity reason webdriver can't load it
                """
                print('[ERRO] Ops.. apparrently the domain provided by server and the current domain are incoherent')
                input('Log in your account and after press <ENTER>')

            except TypeError:
                input('Log in your account and after press <ENTER>')
                

            
            """
            Actions to upload  video...
            """ 

            if driver.title.find('Log in') != -1: #Your authentication fail
                input('Log in and after press <ENTER>')
            
            driver.get(self.upload_url) #Open upload link
            sleep(3)

            buttons = driver.find_element(By.XPATH, "//div[text()='Select file']")
            buttons.send_keys(VIDEO_PATH)
            #Upload video

            driver.find_element(By.XPATH, "//div[text()='Post']").click()
            #Video uploaded


        
        except:
            #Update cookies
        
            mode = input('Do you want to save cookies before left(Y/N)?')
            if mode == 'Y' or 'y':
                self.HG.putCookies(self.account_id, self.C.get_cookies())
                print('Cookies updated')
                driver.quit()
            
            
            
