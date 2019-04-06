import unittest
from pyunitreport import HTMLTestRunner

from socialchains.core.constants import *
from socialchains.pageobjects.pagefactory import *
from socialchains.testbase.testbase import TestBase


class SocialChainsTest(TestBase):

    def test_verify_signIn(self):
        '''Test to verify Sign In'''
        self.driver.get(URL)
        self.driver.click_element('link_text', 'SIGN IN')
        #self.driver.click_element('css', "form[class='login'] input#email")
        element_email = find_element_byCSS(self.driver,"form[class='login'] input#email")
        element_email.click()
        element_email.send_keys("test@gmail.com")
        element_password=find_element_byCSS(self.driver,"form[class='login'] input#password")
        element_email.click()
        element_password.send_keys("Test1")
        #element_button=self.driver.find_element_by_class_name("btn btn-primary register_btt bttn")
        #element_button.click()


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main(testRunner=HTMLTestRunner(output='output_dir', report_name='Social Chains'))