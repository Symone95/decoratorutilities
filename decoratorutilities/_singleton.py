from functools import wraps
__all__ = ['singleton']


class Singleton(object):

    def __init__(self, klass, *args, **kwargs):
        self.name = klass.__name__
        self.instance = klass()
        if len(kwargs) > 0:
            for kwarg in kwargs:
                setattr(self.instance, kwarg, kwargs[kwarg])

    def __call__(self, *args, **kwargs):
        raise TypeError(f'{self.name} object is a singleton not instantiable')

    def __getattr__(self, item):
        return getattr(self.instance, item)


def singleton(*args, **kwargs):

    def class_wrapper(klass):

        @wraps(klass)
        def wrapper():
            return Singleton(klass, *args, **kwargs)

        return wrapper()

    return class_wrapper
