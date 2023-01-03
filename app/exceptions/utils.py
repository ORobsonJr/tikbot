from app.exceptions.webdriver import chrome_version_exception, cookie_exception



def type_error(exception):
    """
    These function is important because selenium usually return just a "webdriverexception" but not specify 
    the exception in question, and for this reason this def was created.

    To identify the specific exception and raise a custom exception.
    """
    exception = str(exception)

    if exception.find('This version of ChromeDriver only supports Chrome version') !=1:#The error indicated
            raise chrome_version_exception('Please verify is the version of webdriver is compatible with your chrome version')

    if exception.find("invalid argument: missing 'cookie'") !=1:
            raise cookie_exception('The cookie provided is not working')

        