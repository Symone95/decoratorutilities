import datetime
from functools import wraps


def timeit(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        tmp = fn(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        print(f"[{fn.__module__}.{fn.__qualname__}] Execution time: {duration.microseconds / 1000} ms")
        return tmp

    return wrapper
