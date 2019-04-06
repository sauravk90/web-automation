import unittest
from pyunitreport import HTMLTestRunner
from Driver import Driver
from Helper import Helper
from Constants import *
from PageFactory import *

class SocialChainsTest(unittest.TestCase):

    def test_verify_signIn(self):
        '''Test to verify Sign In'''
        d = Driver()
        d.driver.get(URL)
        element_click(d.driver,SIGN_IN)
        element_email = find_element_byCSS(d.driver,"form[class='login'] input#email")
        element_email.click()
        element_email.send_keys("test@gmail.com")
        element_password=find_element_byCSS(d.driver,"form[class='login'] input#password")
        element_email.click()
        element_password.send_keys("Test1")
        element_button=d.driver.find_element_by_class_name("btn btn-primary register_btt bttn")
        element_button.click()

        #Assert
        d.driver.close()

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main(testRunner=HTMLTestRunner(output='output_dir', report_name='Social Chains'))