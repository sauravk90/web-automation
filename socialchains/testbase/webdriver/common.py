import time
from socialchains.core.exceptions import IncorrectSelectorType, ElementNotFound


def _find_webelement(root, selector_type, selector_value, element_name, timeout=0):
    """Finds a web element till timed out"""

    webelement = None
    start_time = time.time()
    remaining_time = lambda: timeout - (time.time() - start_time)

    while webelement is None:
        try:
            if selector_type == 'id':
                webelement = root.find_element_by_id(selector_value)
            elif selector_type == 'css':
                webelement = root.find_element_by_css_selector(selector_value)
            elif selector_type == 'link_text':
                webelement = root.find_element_by_link_text(selector_value)
            elif selector_type == 'partial_link_text':
                webelement = root.find_element_by_partial_link_text(selector_value)
            elif selector_type == 'name':
                webelement = root.find_element_by_name(selector_value)
            elif selector_type == 'xpath':
                webelement = root.find_element_by_xpath(selector_value)
            elif selector_type == 'tag_name':
                webelement = root.find_element_by_tag_name(selector_value)
            else:
                msg = 'Selector {} is not a valid option'.format(selector_type)
                raise IncorrectSelectorType(msg)
        except:
            if remaining_time() <= 0:
                break
            else:
                time.sleep(0.5)
                raise ElementNotFound('Element not found yet, remaining time: {:.2f}'
                                       .format(remaining_time()))
    if webelement is None:
        raise ElementNotFound('Element {0} not found using selector {1}:\'{2}\''
                              .format(element_name, selector_type, selector_value))
    else:
        return webelement