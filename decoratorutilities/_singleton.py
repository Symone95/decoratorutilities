from functools import wraps
__all__ = ['singleton']


class Singleton(object):
    """
    Decorate your own classes with **@singleton()** decorator to ensure that only one instance of the singleton class ever exists.
    Never invoke **@singleton()** decorator without brackets otherwise it will cause problems
    Define your class method `__init__()` without parameter, pass them to the **@singleton()** decorator in the format "key" = "value" like kwargs.
    """

    def __init__(self, klass, *args, **kwargs):
        self.args = {}
        self.klass_name = klass.__name__
        if len(args) > 0:
            for index, arg in enumerate(args):
                self.__setitem__(str(index), arg)

        if len(kwargs) > 0:
            for kwarg in kwargs:
                setattr(self, kwarg, kwargs[kwarg])

        obj = klass()
        self.__dict__.update(obj.__dict__)  # Merge args and kwargs with Singleton object

        # Merge decorated class methods with Singleton object
        object_methods = [method_name for method_name in dir(obj)
                          if callable(getattr(obj, method_name))]
        for m in object_methods:
            if not m.startswith("__"):
                setattr(self, m, getattr(obj, m))

    def __call__(self, *args, **kwargs):
        raise TypeError(f'\"{self.klass_name}\" object is a singleton not instantiable')

    def __setitem__(self, key, value):
        self.args[key] = value

    def __getitem__(self, item):
        # If item is digit return item in "self.keys" dict with that index
        if isinstance(item, int):
            if item <= len(self.args):
                return self.args[str(item)]
            else:
                raise IndexError(f"Index: \"{item}\" not found in {self.klass_name} class")
        elif isinstance(item, str):
            if item in self.args:
                return self.args[item]
            else:
                raise KeyError(f"Key: \"{item}\" not found in {self.klass_name} class")

    def __delitem__(self, key):
        del self.args[key]

    def __str__(self):
        return self.klass_name

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

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

    :param args: Class method *args
    :param kwargs: Class method **kwargs
    :return: Singleton instance of decorated class
    :raise: TypeError if klass is not a class method
    """

    @wraps(Singleton)
    def class_wrapper(klass):

        if not str(klass).startswith("<class "):
            raise TypeError("Singleton decorator applicable on class only")
        return Singleton(klass, *args, **kwargs)  # wrapper()
    return class_wrapper
