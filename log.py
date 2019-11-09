
import os
import logging


def setup(log_name, log_to_console=True, log_to_file=False, dirname=None):
    handlers = []

    formatter = _configure_formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if log_to_console:
        console_handler = _configure_console_handler(logging.WARNING, formatter)
        handlers.append(console_handler)

    elif log_to_file:
        if not dirname:
            raise AttributeError('if log_to_file is True, a dirname should be passed as well')
        try:
            file_handler = _configure_file_handler(logging.INFO, formatter,
                                                   os.path.join(dirname, '%s.log' % log_name))
            handlers.append(file_handler)
        except IOError:
            raise  # re-raise _is_valid_location's exception

    else:
        raise AttributeError('At least one handler must been choose.')

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
        raise IOError('"location" is not valid. Check if exists or is a dir')

    handler = logging.FileHandler(location)
    handler.setLevel(level)

    handler.setFormatter(formatter)

    return handler


def _location_is_valid(location):
    if not os.path.exists(location) or not os.path.isdir(location):
        return False
    return True
