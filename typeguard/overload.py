from functools import wraps

def overload(fn):


    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    