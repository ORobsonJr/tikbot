import yaml



with open('tiktok.yaml') as f:
    #Return content
    self.data = yaml.load(f, Loader=yaml.FullLoader)
            

def root_route():
    #Return tiktok link
    return self.data['ROUTE']

def upload_route():
    #Return tiktok upload link 
    return self.data['UPLOAD-ROUTE']
