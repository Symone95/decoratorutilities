from ._checktype import checktype
from ._overload import overload
from ._mocking import mocking
from ._cached import cached
from ._timeit import timeit
from ._singleton import singleton
from ._debug import debug

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("decoratorutilities")


def is_class_method(arg):
    # Controllo se il parametro passato è una funzione o un metodo di una classe - args[0]
    return "__module__" in dir(arg) and arg.__module__ is not None
