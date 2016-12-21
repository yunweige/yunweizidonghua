'''
import logging

def use_logging(func):
    logging.warn("%s is running" % func.__name__)


def bar():
    print('i am foo')


def use_logging(func):
    def wrapper(*argsm **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper



use_logging(bar)


'''

