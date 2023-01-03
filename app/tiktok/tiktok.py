from app.tiktok.uploader import UPLOAD
from app.exceptions import utils
from app.api.getAPI import handleAPI
from app.tiktok.config.settings import configure


def run_tiktok_feature(self, account_id_: str, video: str = ''):
    try:
        if video:
            UPLOAD(account_id_).__main__(video)
            return

        
        UPLOAD(account_id_).__main__()
    except Exception as e:
        handleAPI().putCookies(account_code=account_id_, cookies=configure(account_id_).get_cookies()) #Update cookies before crash
        t = utils.type_error(e) #Raise error

