import pytest
from decoratorutilities import singleton


def test_singleton_class_no_params():

    @singleton()
    class A(object):
        def __init__(self):
            self.x = 10

        def print_hello(self):
            return "Hello World"

    assert A.x == 10
    assert A.print_hello() == "Hello World"

    with pytest.raises(TypeError):
        @singleton
        class B(object):
            def __init__(self):
                self.x = 10

        B()  # Raises TypeError Exception


def test_singleton_class_with_kwargs():

    @singleton(x=10, message="Message to send", email=["simone.scalamandre95@gmail.com"])
    class A(object):
        pass

    assert A.x == 10
    assert A.message == "Message to send"
    assert len(A.email) == 1
    assert A.email == ["simone.scalamandre95@gmail.com"]


def test_singleton_instantiation_fails():

    @singleton()
    class A(object):
        def __init__(self):
            pass

    @singleton(x=10)
    class B(object):
        def __init__(self):
            pass

    with pytest.raises(TypeError) as e:
        A()

    with pytest.raises(TypeError):
        B()
