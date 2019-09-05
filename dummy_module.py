#!/usr/bin/env python
# coding: utf-8

import os
import log

here = os.path.dirname(__file__)

logger = log.setup(log_name='dummy', log_to_console=True, 
            log_to_file=True, dirname=os.path.join(here, 'logs'))

def foo():
    logger.warning('some shit might be happen soon...')
    logger.info('everything is normal')

foo()