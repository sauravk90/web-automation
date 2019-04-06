import time

from testbase.constants import *


class Helper:
    '''
    Helper class with static methods to facilitate direct use from within unit tests
    '''

    @staticmethod
    def verify_file_downloaded(filename):
        '''
        Checks id report file has been downloaded in the DOWNLOAD_PATH,
        raises an FileNotFoundError if timed out (default is 10 sec)
        :param filename:
        :return: True or False
        '''
        timeout = 10
        i = 0
        while i<=timeout:
            if os.path.isfile(DOWNLOAD_PATH + filename):
                print('Report {} was successfully saved...'.format(filename))
                return
            else:
                print('Waiting {} more seconds before timeout...'.format(timeout-i))
                time.sleep(1)
                i += 1
                continue

        raise FileNotFoundError('File {} does not exist after {} sec timeout'.format(filename, timeout))

    @staticmethod
    def verify_report(file, cons_pos_size_file, max_perm_lev_file, max_perm_short_pos_file, trail_stop_loss_max_daily_loss_file):
        '''
        Helper method to verify content of the PDF report downloaded
        :param file:
        :param cons_pos_size_file:
        :param max_perm_lev_file:
        :param max_perm_short_pos_file:
        :param trail_stop_loss_max_daily_loss_file:
        :return: True or False
        '''
       # p = PDFReader()
        #return p.verify_report(DOWNLOAD_PATH + file, cons_pos_size_file, max_perm_lev_file,
                               #max_perm_short_pos_file, trail_stop_loss_max_daily_loss_file)