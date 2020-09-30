__all__ = ['singleton']


class Singleton(object):

    def hello(self):
        return 'world'

    def __init__(self, klass, *args, **kwargs):
        self.instance = klass(*args, **kwargs)
        self.name = klass.__name__
        return klass.__init__()

    def __call__(self, *args, **kwargs):
        raise TypeError(f'{self.name} object is a singleton not instantiable')

    def __getattr__(self, item):
        return getattr(self.instance, item)


def singleton(klass, *args, **kwargs):# klass, *pargs, **pkwargs):

    print("klass: ", klass)
    print("INIT: ", klass.__init__)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("klass ANNOTATIONS: ", klass.__init__.__annotations__)
    print("klass ANNOTATIONS: ", len(klass.__init__.__annotations__))

    def wrapper(*aargs):
        print("klass: ", klass)
        print("type klass: ", type(klass))

        print("args INSIDE: ", aargs)

        if args:
            print("args: ", args)
            print("CLASS: ", args[0], " - TYPE: ", type(args[0]))  #, " - DIR: ", dir(args[0]))
            x = args[0]
            print("x: ", x)

        if kwargs:
            print("kwargs: ", kwargs)

        print("klass: ", klass)
        print("type klass: ", type(klass))
        print("args: ", args)
        print("kwargs: ", kwargs)
        return Singleton(klass, *args, **kwargs)

    return wrapper()
    #print("LUNGHEZZA: ", (len(args) > 1))
    #return wrapper if len(args) > 1 else Singleton(klass, *args, **kwargs)  # klass

"""
def singleton(*args, **kwargs):
    if args:
        #print("args: ", args)
        print("CLASS: ", args[0])
        print("TYPE: ", type(args[0]))
        print("kwargs: ", kwargs)
        x = args[0]
        print("x: ", x)

    def wrapper(klass):
        print("klass: ", klass)
        return Singleton(klass, *args, **kwargs)

    return wrapper
"""
