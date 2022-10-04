from os.path import dirname, abspath
from json import load
#from vars.variable import LOCAL


class LOCAL():
    def __init__(self) -> None:
        from os.path import dirname, abspath

        file_ = dirname(abspath("app"))+'/app/vars/api.json'
        with open(file_) as f:
            self.raw_content = load(f)
            f.close() 

    def url(self):
        url = self.raw_content['raw_url'] #Get the raw url, in our case; localhost
        port = self.raw_content['port'] #Get the port that is running
        return url + port






