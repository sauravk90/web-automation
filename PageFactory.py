import time
from Driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants import *
'''
Class to store Selenium WebElements and perform some generic actions on those,
can be called directly from within unit tests
'''
def element_click(driver,locator):
    '''
    Clicks on the locator after waiting for duration specified under DEFAULT_WAIT.
    :param driver:
    :param locator
    :return: None
    '''
    wait = WebDriverWait(driver, DEFAULT_WAIT)
    element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,locator)))
    element.click()



def find_element_byCSS(driver,locator):
    '''
    :param driver:
    :param locator :
    :return: WebElement
    '''
    wait = WebDriverWait(driver, DEFAULT_WAIT)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    return element