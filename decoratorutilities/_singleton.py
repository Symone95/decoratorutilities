class Singleton(object):

    def hello(self):
        return 'world'

    def __init__(self, klass, *args, **kwargs):
        self.instance = klass(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        raise TypeError(f'{self.instance.__name__} object is a singleton not instantiable')
    #
    # def __getitem__(self, item):
    #     return self.instance.__getitem__(item)

    def __getattr__(self, item):
        return getattr(self.instance, item)
    #
    # def __getattribute__(self, item):
    #     return self.instance.__getattribute__(item)


def singleton(*args, **kwargs):
    def wrapper(klass):
        print(klass)
        return Singleton(klass, *args, **kwargs)

    return wrapper
