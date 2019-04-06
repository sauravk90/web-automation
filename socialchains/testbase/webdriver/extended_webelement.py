# from typing import List # not supported in 3.4
import time

from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement
from selenium.webdriver.firefox.webelement import FirefoxWebElement
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select as SeleniumSelect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from socialchains.testbase.webdriver.common import _find_webelement


class ExtendedWebElement:

    selector_type = None
    selector_value = None
    name = None

    def check(self):
        """Check element if element is checkbox or radiobutton.
        If element is already checked, this is ignored.
        """
        checkbox_or_radio = (self.tag_name == 'input' and
                             self.get_attribute('type') in ['checkbox', 'radio'])
        if checkbox_or_radio:
            if not self.is_selected():
                self.click()
        else:
            msg = 'Element {} is not checkbox or radiobutton'.format(self.name)
            raise ValueError(msg)

    def double_click(self):
        """Double click the element"""
        action_chains = ActionChains(self.parent)
        action_chains.double_click(self).perform()

    def focus(self):
        """Give focus to element"""
        self.parent.execute_script('arguments[0].focus();', self)

    def has_attribute(self, attribute):
        """Returns whether element has attribute"""
        return self.get_attribute(attribute) is not None

    def has_focus(self):
        """Returns whether element has focus"""
        script = 'return arguments[0] == document.activeElement'
        return self.parent.execute_script(script, self)

    @property
    def inner_html(self):
        """"Element innerHTML attribute"""
        return self.get_attribute('innerHTML')

    def javascript_click(self):
        """Click element using Javascript"""
        self.parent.execute_script('arguments[0].click();', self)

    def mouse_over(self):
        """Mouse over element"""
        action_chains = ActionChains(self.parent)
        action_chains.move_to_element(self).perform()

    @property
    def outer_html(self):
        """"Element outerHTML attribute"""
        return self.get_attribute('outerHTML')

    def press_key(self, key):
        """Press a key on element

        :Usage:
          element.press_key('ENTER')
          element.press_key('TAB')
          element.press_key('LEFT')
        """
        if hasattr(Keys, key):
            key_attr = getattr(Keys, key)
            self.send_keys(key_attr)
        else:
            defined_keys = [name for name in dir(Keys) if
                            not name.startswith('_')]
            error_msg = ('Key {} is invalid\n'
                         'valid keys are:\n'
                         '{}'.format(key, ','.join(defined_keys)))
            raise ValueError(error_msg)


    def send_keys_with_delay(self, value, delay=0.1):
        """Send keys to element one by one with a delay between keys """
        if not isinstance(delay, int) and not isinstance(delay, float):
            raise ValueError('delay must be int or float')
        elif delay < 0:
            raise ValueError('delay must be a positive number')
        else:
            for c in value:
                self.send_keys(c)
                time.sleep(delay)

    def uncheck(self):
        """Uncheck element if element is checkbox """
        is_checkbox = (self.tag_name == 'input' and
                       self.get_attribute('type') == 'checkbox')
        if is_checkbox:
            if self.is_selected():
                self.click()
        else:
            raise ValueError('Element {} is not checkbox'.format(self.name))

    @property
    def value(self):
        """The value attribute of element"""
        return self.get_attribute('value')

    def wait_displayed(self, timeout=30):
        """Wait for element to be displayed

        :Returns:
          The element
        """
        wait = WebDriverWait(self.parent, timeout)
        message = ('Timeout waiting for element {} to be displayed'
                   .format(self.name))
        wait.until(ec.visibility_of(self), message=message)
        return self
