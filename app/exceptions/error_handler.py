from selenium.common.exceptions import NoSuchElementException

"""
We've the exceptions and we've the solutions to these exceptions.

This file handle these exceptions and try fix them.
"""

def ChromeDriverVersion(exception_traceback):
    """
    Serves to correct the Undetected_chromedriver exception, where return message: "This version of ChromeDriver only supports Chrome version ..."

    In current version of this library, a solution which we can follow according to the documentation (https://github.com/ultrafunkamsterdam/undetected-chromedriver#words-of-wisdom)
    is adding an argument while create driver object named "version_main".

    We could simply add our argument in hard-code way, buy it's a bad pratice, then here we'll get the version of machine which is running and provided to driver object.
    """

    find = 'Current browser version is ' #The argument to try find
    exception_traceback = str(exception_traceback) #Transform the exception in string format

    if exception_traceback.find(find) !=-1: #The error
        """
        How here works

        Find index from "Current browser version is"
        find index from "Stacktrace:"

        The version (106.0...) is between these filters
        Return the 3 first numbers which is what we'll use
        """
        index = 27 #The index of message
        browser_index = exception_traceback.find(find)+index  
        stacktrace = exception_traceback.find('Stacktrace:') #Find by stacktrace message
        final_version = exception_traceback[browser_index:stacktrace-1] #Get the final version of webdriver, ex.: 106.0.5249.103
        #Return the 3 first numbers in int format, we'll uses them posteriorly to avoid 
        #the exception chrome driver version.
        return int(final_version[:3])


