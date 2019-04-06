"""This module defines custom exceptions used by the test cases"""


class IncorrectSelectorType(Exception):
    pass

class ElementNotFound(Exception):
    pass

class TextNotPresent(Exception):
    pass

class ElementNotDisplayed(Exception):
    pass