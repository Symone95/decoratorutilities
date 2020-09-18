from functools import wraps


def mocking(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        pass
