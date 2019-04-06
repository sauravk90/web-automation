from selenium import webdriver
from pathlib import Path
from socialchains.core.constants import *
from socialchains.testbase.webdriver import TestChromeDriver

class Driver(TestChromeDriver):
    '''
    Custom Selenium WebDriver initialization class
    '''
    def __init__(self):
        self.driver = None

    def getbrowser(self):
        if not isinstance(self.driver, TestChromeDriver):
            chrome_options = webdriver.ChromeOptions()
            #options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            prefs = {'download.default_directory': DOWNLOAD_PATH}
            chrome_options.add_experimental_option('prefs', prefs)

            chromedriver_path = str(Path(__file__).parent / "../../.." / "drivers" / "chromedriver.exe")
            self.driver = TestChromeDriver(executable_path=chromedriver_path, options=chrome_options)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)

        return self.driver