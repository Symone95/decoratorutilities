from decoratorutilities import debug
import pytest


def test_function_debug():

    @debug
    def a():
        message = "Hello " + 5
        return message

    with pytest.raises(TypeError):
        a()


def test_class_debug_method():

    class A(object):

        @debug
        def __init__(self):
            self.message = "Hello " + 5

    with pytest.raises(TypeError):
        A()
