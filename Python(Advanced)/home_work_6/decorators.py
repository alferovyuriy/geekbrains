"""Decorators module"""


import sys
import logging
import traceback
from logs import config_client_log, config_server_log


if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func):
    """function decorator"""
    def log_wrapper(*args, **kwargs):
        """wrapper"""
        stack = traceback.extract_stack()
        res = func(*args, **kwargs)
        LOGGER.debug(f'Colled function {func.__name__} with params {args, kwargs}'
                     f'Call from module {func.__module__} function {stack[1].name}')
        return res
    return log_wrapper


class Log:
    """Class decorator"""
    def __call__(self, func):
        """get func object after call decorator"""
        def log_wrapper(*args, **kwargs):
            """wrapper"""
            stack = traceback.extract_stack()
            res = func(*args, **kwargs)
            LOGGER.debug(f'Colled function {func.__name__} with params {args, kwargs}'
                         f'Call from module {func.__module__} function {stack[1].name}')
            return res
        return log_wrapper
