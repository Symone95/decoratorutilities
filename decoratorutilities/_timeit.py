import datetime
from functools import wraps

__all__ = ['timeit']


def timeit(fn):
    """
    MODULE NAME
        timeit

    MODULE REFERENCE
        https://decoratorutilities.readthedocs.io/en/latest/rst_templates/Decorators/timeit_decorator.html

    Decorate your own function with **@timeit** decorator to monitoring execution time

    :param fn: Decorated function or class method to monitoring execution time
    :return:
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        tmp = fn(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        print(f"[{fn.__module__}.{fn.__qualname__}] Execution time: {duration.microseconds / 1000} ms")
        return tmp

    return wrapper
