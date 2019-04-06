import unittest
import logging

from socialchains.testbase.webdriver.driver import Driver

class TestBase(unittest.TestCase):

    def setUp(self):
        logging.info("## SETUP METHOD ##")
        logging.info("# Initializing the webdriver.")
        driver_obj = Driver()
        self.driver = driver_obj.getbrowser()

    def tearDown(self):
        logging.info("## TEARDOWN METHOD ##")
        self.driver.quit()