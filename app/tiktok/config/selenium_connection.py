import undetected_chromedriver.v2 as uc
from selenium.common.exceptions import WebDriverException
from app.vars.variable import LOCAL
from selenium import webdriver
from app.exceptions.error_handler import ChromeDriverVersion
from app.exceptions import utils
from app.exceptions.webdriver import chrome_version_exception

try:
    driver = uc.Chrome() #Try create connection
except WebDriverException as e: 
    try: utils.type_error(e) #Filter webdriver_exception and raise a specific exception

    except chrome_version_exception: 
        version_main_to_use = ChromeDriverVersion(e) #Return version_main to use
        driver = uc.Chrome(executable_path=LOCAL().webdriver_location(), version_main=version_main_to_use)

