#!/usr/bin/env python
# coding: utf-8

"""
LOG LEVELS
==========

DEBUG
Detailed information, typically of interest only when diagnosing problems.

INFO
Confirmation that things are working as expected.

WARNING
An indication that something unexpected happened, or indicative of some problem 
in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR
Due to a more serious problem, the software has not been able to perform some function.

CRITICAL
A serious error, indicating that the program itself may be unable to continue running.
"""

import logging

logger = logging.getLogger(__name__)
# no handler could handle a level higher than the own logger level
# this should be high af
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__ == '__main__':
	logger.debug('This message should not be displayed unless a handler was created')
	logger.warning('Some shit is about to happen...')
	logger.error('Some shit happened.')
	logger.critical('Some SERIOUS shit happened, dude!')
	logger.info('Some chill stuff is happening as expected...')
