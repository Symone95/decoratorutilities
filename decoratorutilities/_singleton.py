from functools import wraps
__all__ = ['singleton']


class Singleton(object):
    """
    Decorate your own classes with **@singleton()** decorator to ensure that only one instance of the singleton class ever exists.
    Never invoke **@singleton()** decorator without brackets otherwise it will cause problems
    Define your class method `__init__()` without parameter, pass them to the **@singleton()** decorator in the format "key" = "value" like kwargs.
    """

    def __init__(self, klass, *args, **kwargs):
        print("SONO NELL'INIT DEL SINGLETON")
        #self.instance = klass  # ()
        #self = klass  # ()
        self.keys = {}
        self.klass_name = klass.__name__

        #print("ISTANZA: ", self.instance)
        print("ARGS: ", args)
        print("KWARGS: ", kwargs)
        if len(args) > 0:
            for index, arg in enumerate(args):
                #setattr(self.instance, str(index), arg)
                #setattr(self, str(index), arg)
                self.__setitem__(str(index), arg)
                #setattr(klass, str(index), arg)

        if len(kwargs) > 0:
            for kwarg in kwargs:
                #setattr(self.instance, kwarg, kwargs[kwarg])
                setattr(self, kwarg, kwargs[kwarg])
                #setattr(klass, kwarg, kwargs[kwarg])

        #self.instance()
        #self()
        klass()
        print("OGGETTO PRONTO")

    def __call__(self, *args, **kwargs):
        raise TypeError(f'\"{self.klass_name}\" object is a singleton not instantiable')
        #raise TypeError(f'{self.instance.__name__} object is a singleton not instantiable')

    """def __getattribute__(self, item):
        print("GETATTRIBUTE: ", item)
        #pass
        #return self.__getitem__(item)
        #return object.__getattribute__(item)
        return getattr(self, item)  # item  #self.__getattribute__(item)"""

    """
    def __getattr__(self, item):
        print("GET ATTR: ", item)
        return super().__getattr__(item)
        #pass
        #return getattr(self, item)  #self.instance.__getattribute__(item) #self.__getattr__(item)  # [item]  # getattr(self.instance, item)  # self.keys[item]

    def __setattr__(self, key, value):
        print("SET ATTR: KEY: ", key, " - VALUE: ", value)
        # self.keys[key] = value
        #setattr(self, key, value)  # .instance
        super().__setattr__(key, value)
    """
    def __setitem__(self, key, value):
        self.keys[key] = value
        #setattr(self.instance, key, value)
        #setattr(self, key, value)

    def __getitem__(self, item):
        # If item is digit return item in "self.keys" dict with that index
        if isinstance(item, int):
            if item <= len(self.keys):
                return self.keys[str(item)]
            else:
                raise IndexError(f"Index: \"{item}\" not found in {self.klass_name} class")
        elif isinstance(item, str):
            if item in self.keys:
                return self.keys[item]
            else:
                raise KeyError(f"Key: \"{item}\" not found in {self.klass_name} class")

    def __delitem__(self, key):
        del self.keys[key]

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

    print("PRIMI ARGS: ", args)
    print("PRIMI KWARGS: ", kwargs)

    @wraps(Singleton)
    def class_wrapper(klass):

        print("PRIMI KLASS: ", klass)

        """@wraps(klass)
        def wrapper():
            print("PRIMI KLASS: ", klass)
            # If klass is not a class method raises TypeError exception
            if not str(klass).startswith("<class "):
                raise TypeError("Singleton decorator applicable on class methods only")
            return Singleton(klass, *args, **kwargs)"""

        print("SONO QUI 2")
        if not str(klass).startswith("<class "):
            raise TypeError("Singleton decorator applicable on class only")

        return Singleton(klass, *args, **kwargs)  # wrapper()
    print("SONO QUI 1")
    return class_wrapper
