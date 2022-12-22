from app.exceptions.webdriver import chrome_version_exception, cookie_exception

def type_error(exception):
    """Define which type of exception we're dealing"""
    exception = str(exception)

    if exception.find('This version of ChromeDriver only supports Chrome version') !=1:#The error indicated
            raise chrome_version_exception('Please verify is the version of webdriver is compatible with your chrome version')

    if exception.find("invalid argument: missing 'cookie'") !=1:
            raise cookie_exception('The cookie provided is not working')

        