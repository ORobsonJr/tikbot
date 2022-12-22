from selenium.common.exceptions import WebDriverException



class chrome_version_exception(Exception):
    """
    Problem with current version of chrome driver

    note.: Not every error is associated with webdriver version, sometimes
    this is connected to some exception during an attempt to realize some action using selenium.

    If selenium open the browser and open the link properly the problem isn't connected to webdriver version.


    """

class cookie_exception(Exception):
    """
    Problem in attempt to add cookies to session
    
    Probrably a malformed cookies or a invalid session provided.
    """





    