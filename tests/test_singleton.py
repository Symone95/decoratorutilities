import pytest
from decoratorutilities import singleton


def test_singleton_class():

    #@singleton(klass="C")
    @singleton
    class A(object):
        def __init__(self, c, prova: str):
            self.x = 10
            self.prova = prova

    #@singleton("Prov", "SImone", nome="SIMO")
    #def test():
    #    pass

    """
    @singleton
    class B(object):
        def __init__(self):
            self.x = 50
    """

    #print(A)
    #assert A.x == 10


"""

def test_singleton_class_constructor():

    @singleton(x=10)
    class A(object):
        def __init__(self, x):
            self.x = x

    assert A.x == 10
    A.x = 9

    assert A.x == 9


def test_singleton_instantiation_fails():

    @singleton
    class A(object):
        def __init__(self):
            pass

    @singleton(x=10)
    class B(object):
        def __init__(self, x):
            pass

    with pytest.raises(TypeError):
        A()

    with pytest.raises(TypeError):
        B()

"""