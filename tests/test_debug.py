from decoratorutilities import debug
import pytest


def test_add_function():

    @debug
    def add(a, b):
        return a + b


    add(1, 2)
    add('a', 'b')
    with pytest.raises(TypeError):
        add('a', 1)


def test_function_debug_no_parameter():

    @debug
    def a():
        message = "Hello " + 5
        return message

    with pytest.raises(TypeError):
        a()


def test_function_debug_with_parameter():

    @debug
    def my_fun(param1: int):
        message = "Hello " + param1
        return message
    with pytest.raises(TypeError):
        my_fun(1)


def test_class_debug_method():

    class A(object):

        @debug
        def __init__(self):
            self.message = "Hello " + 5

    class B(object):

        @debug
        def send_message(self, message: str, email_addresses: tuple):
            return message + email_addresses

    with pytest.raises(TypeError):
        A()

    with pytest.raises(TypeError):
        B().send_message("My message", ("foe@gmail.com", "friend@gmail.com"))
