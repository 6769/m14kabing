# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 02:12:40 2017

@author: pipi6
"""
__VERSION__ = 1.0

import logging
import sys

DEFAULT_FILENAME = 'run.log'
DEFAULT_FORMAT = '%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s'
DEFAULT_FILECHARPAGE = 'UTF-8'

#Singleton Pattern
try:
    exist_logger
except NameError:
    exist_logger = dict()


def getloggerfast(hisname: str,
                  logfname: str = DEFAULT_FILENAME) -> logging.Logger:
    """
    Fastly generate a logger which contains log to Console and File named `run.log`.
    
    Parameters
    ----
    hisname: str
        the sigunature to retrieve logger.
    logfname: str
        the filename which log infomation will be written to,
        DEFAULT_FILENAME:run.log.
        
    Examples
    --------
    
    >>> lo=getloggerfast(__name__)
    >>> _testlib()
    {'__main__': <Logger __main__ (DEBUG)>}
    >>> lo.debug('debug message') # info also dump to file `run.log`
    2017-10-04 04:05:14,375 - __main__ - INFO     - info message
        
        
    """
    if hisname in exist_logger.keys():
        return exist_logger[hisname]

    # create logger
    logger = logging.getLogger(hisname)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)

    fh = logging.FileHandler(logfname, encoding=DEFAULT_FILECHARPAGE)
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(DEFAULT_FORMAT)

    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    exist_logger[hisname] = logger
    return logger


def _testlib():
    print(exist_logger)


if __name__ == '__main__':
    lo = getloggerfast(__name__)
    _testlib()
    # 'application' code
    lo.debug('debug message')
    lo.info('info message')
    lo.warning('warn message')
    lo.error('error message')
    lo.critical('critical message')
