from selenium.webdriver import Chrome as SeleniumChromeDriver
from socialchains.testbase.webdriver.extened_driver import ExtendedDriver

class TestChromeDriver(SeleniumChromeDriver, ExtendedDriver):
    pass