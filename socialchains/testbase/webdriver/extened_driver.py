from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

from socialchains.testbase.webdriver.common import _find_webelement
from socialchains.core.exceptions import ElementNotFound, ElementNotDisplayed


class ExtendedDriver:
    """ A custom implementation of Selenium Webdriver """

    def click_element(self, selector_type, selector_value, element_name="Element", timeout=0):
        element = _find_webelement(self, selector_type, selector_value, element_name, timeout=0)
        element.click()

    def accept_alert(self, ignore_not_present=False):
        try:
            self.switch_to.alert.accept()
        except NoAlertPresentException:
            if not ignore_not_present:
                raise

    def alert_is_present(self):
        """Returns whether an alert is present"""
        try:
            self.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def check_element(self, element):
        """Check an element (checkbox or radiobutton).
        If element is already checked this is ignored.
        """
        element = self.find(element)
        element.check()

    def close_window_by_title(self, title):
        """Close window/tab by title"""
        titles = self.get_window_titles()
        if title in titles:
            handle_to_close = self.window_handles[titles.index(title)]
            self.close_window_switch_back(handle_to_close)
        else:
            raise ValueError('a window with title {} was not found'.format(title))

    def dismiss_alert(self, ignore_not_present=False):
        try:
            self.switch_to.alert.dismiss()
        except NoAlertPresentException:
            if not ignore_not_present:
                raise

    def element_is_present(self, element):
        """If element is present, return the element"""
        try:
            element = self.find(element, timeout=0)
            return element
        except ElementNotFound:
            return False

    def drag_and_drop(self, element, target):
        actionChains = ActionChains(self)
        source_element = self.find(element)
        target_element = self.find(target)
        actionChains.drag_and_drop(source_element, target_element).perform()

    def get_window_titles(self):
        """Return a list of the titles of all open windows/tabs"""
        original_handle = self.current_window_handle
        titles = []
        for handle in self.window_handles:
            self.switch_to.window(handle)
            titles.append(self.title)
        self.switch_to.window(original_handle)
        return titles

    def navigate(self, url):
        """Alternative to driver.get()"""
        self.get(url)

    def switch_to_window_by_index(self, index):
        """ Switch to window/tab by index """
        self.switch_to.window(self.window_handles[index])


    def wait_for_element_displayed(self, element, timeout):
        """ Wait for element to be present and displayed """
        try:
            element = self.find(element, timeout=timeout, wait_displayed=True)
        except ElementNotDisplayed:
            message = ('timeout waiting for element {} to be displayed'
                       .format(element))
            raise TimeoutException(message)

    def wait_for_element_enabled(self, element, timeout):
        """Wait for element to be enabled """
        element = self.find(element, timeout=0)
        return element.wait_enabled(timeout)

    def wait_for_element_not_present(self, element, timeout):
        """Wait for element not present in the DOM """
        found_element = None
        try:
            found_element = self.find(element, timeout=0)
        except ElementNotFound:
            pass
        if found_element:
            wait = WebDriverWait(self, timeout)
            message = ('Timeout waiting for element {} to not be present'
                       .format(found_element.name))
            wait.until(ec.staleness_of(found_element), message=message)

    def wait_for_element_present(self, element, timeout):
        """Wait for element present in the DOM """
        try:
            self.find(element, timeout=timeout, wait_displayed=False)
        except ElementNotFound:
            message = ('timeout waiting for element {} to be present'
                       .format(element))
            raise TimeoutException(message)

    def wait_for_element_text(self, element, text, timeout):
        """Wait for element text to match given text """
        element = self.find(element, timeout=0)
        return element.wait_text(text, timeout)
