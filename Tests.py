import unittest
from pyunitreport import HTMLTestRunner
from Driver import Driver
from Helper import Helper
from Constants import *
from PageFactory import *

class GoogleTest(unittest.TestCase):

    def test_file_upload(self):
        '''Test to verify csv file upload functionality'''
        d = Driver()
        d.driver.get(URL)
        upload_file(d.driver, TEST_DATA_PATH + 'csv\\test.csv')

        #Assert
        d.driver.close()

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main(testRunner=HTMLTestRunner(output='output_dir', report_name='Google'))