from functools import wraps


def cached(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):

        return fn(*args, **kwargs)

    return wrapper
