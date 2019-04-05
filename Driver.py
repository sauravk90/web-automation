from selenium import webdriver
from Constants import *

class Driver:
    '''
    Selenium WebDriver initialization class
    '''
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': DOWNLOAD_PATH}
        chrome_options.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(executable_path=r'drivers\chromedriver.exe', options=chrome_options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)