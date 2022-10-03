

class IDENT():
    def __init__(self, account_id: str = ''):
        self.id = account_id

    def return_data(self, identify_code: str):
        from os.path import dirname, abspath
        from json import load as read

        root_location = dirname(abspath("app"))
        file_location = root_location + '/../database/identities/' + identify_code+'.json'

        try:
            with open(file_location) as f:
                return read(f)
        except FileNotFoundError:
            return 'The identify code is invalid, try a accounts that exists'