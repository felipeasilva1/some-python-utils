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

import os
import logging

def setup(log_name, log_to_console=True, log_to_file=False, dirname=None):

    handlers = []

    formatter = _configure_formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if log_to_console:
        console_handler = _configure_console_handler(logging.WARNING, formatter)
        handlers.append(console_handler)

    if log_to_file:
        if not dirname:
            raise Exception('if log_to_file is True, a dirname should be passed as well')
        file_handler = _configure_file_handler(logging.INFO, formatter, 
                            os.path.join(dirname, '%s.log' % log_name))
        handlers.append(file_handler)

    logger = _configure_logger(log_name, logging.DEBUG, handlers)

    return logger

def _configure_logger(log_name, default_level, handlers):

    logger = logging.getLogger(log_name)
    logger.setLevel(default_level)

    for handler in handlers:
        logger.addHandler(handler)

    return logger

def _configure_formatter(message_format):
    return logging.Formatter(message_format)

def _configure_console_handler(level, formatter):

    handler = logging.StreamHandler()
    handler.setLevel(level)

    handler.setFormatter(formatter)

    return handler

def _configure_file_handler(level, formatter, location):

    if not _location_is_valid(location):
        raise

    handler = logging.FileHandler(location)
    handler.setLevel(level)

    handler.setFormatter(formatter)

    return handler

def _location_is_valid(location):
    return True