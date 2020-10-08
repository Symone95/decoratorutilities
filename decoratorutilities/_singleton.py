from functools import wraps
__all__ = ['singleton']


class Singleton(object):

    def __init__(self, klass, *args, **kwargs):
        self.name = klass.__name__
        self.instance = klass()
        if len(args) > 0:
            for index, arg in enumerate(args):
                setattr(self.instance, str(index), arg)

        if len(kwargs) > 0:
            for kwarg in kwargs:
                setattr(self.instance, kwarg, kwargs[kwarg])

    def __call__(self, *args, **kwargs):
        raise TypeError(f'{self.name} object is a singleton not instantiable')

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setitem__(self, key, value):
        setattr(self.instance, key, value)

    def __getitem__(self, item):
        return getattr(self.instance, item)

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.instance)

    def __enter__(self):
        self.fp = open(self.filename, "a+")
        return self.instance

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


def singleton(*args, **kwargs):
    """
    MODULE NAME
        singleton

    MODULE REFERENCE
        https://decoratorutilities.readthedocs.io/en/latest/rst_templates/Decorators/singleton_decorator.html

    Decorate your own classes with **@singleton()** decorator to ensure that only one instance of the singleton class ever exists.
    Never invoke **@singleton()** decorator without brackets otherwise it will cause problems
    Define your class method `__init__()` without parameter, pass them to the **@singleton()** decorator in the format "key" = "value" like kwargs.

    :param args:
    :param kwargs:
    :return:
    """

    def class_wrapper(klass):

        @wraps(klass)
        def wrapper():
            return Singleton(klass, *args, **kwargs)

        return wrapper()

    return class_wrapper
