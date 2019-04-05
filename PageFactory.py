import time
'''
Class to store Selenium WebElements and perform some generic actions on those,
can be called directly from within unit tests
'''

def upload_file(driver, file_path):
    '''
    Uploads file from file_path
    :param driver:
    :param file_path:
    :return: None
    '''
    try:
        driver.find_element_by_xpath(upload_button_xpath).send_keys(file_path)
    except:
        print('In except')
        driver.find_element_by_xpath('/html/body').send_keys(file_path)
    finally:
        time.sleep(10)

def download_report(driver):
    '''
    Clicks on the donload button to donwload Report file
    :param driver:
    :return: None
    '''
    driver.find_element_by_xpath(download_button_xpath).click()

