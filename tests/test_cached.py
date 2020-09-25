import datetime

import pytest
from decoratorutilities import cached


# def test_no_parameters():
#
#     """
#     @cached
#     def fun(p1: str):
#         return p1
#     """
#
#     call_count = 0
#
#     @cached
#     def fn():
#         global call_count
#         call_count += 1
#
#     assert call_count == 0
#
#     fn()
#
#     assert call_count == 1
#
#     fn()
#
#     assert call_count == 1

call_count_param1 = 0
call_count_param2 = 0


def test_with_parameters():

    @cached
    def fn(value: int):
        global call_count_param1
        global call_count_param2

        if value == 1:
            call_count_param1 += 1

        if value == 2:
            call_count_param2 += 1

    assert call_count_param1 == 0
    assert call_count_param2 == 0

    fn(1)

    assert call_count_param1 == 1
    assert call_count_param2 == 0

    fn(1)

    assert call_count_param1 == 1
    assert call_count_param2 == 0

    fn(2)

    assert call_count_param1 == 1
    assert call_count_param2 == 1


def test_cached_class():

    class X(object):

        @cached
        def x(self):
            return 1

    class Y(object):

        @cached
        def x(self):
            return 2

    assert X().x() == 1
    assert Y().x() == 2


def test_cached_class_parameters():

    class X(object):

        @cached
        def x(self, value):
            return value

    class Y(object):

        @cached
        def x(self, value):
            return value

    x = X()
    y = Y()
    assert x.x(1) == 1
    assert y.x(2) == 2
    assert x.x(2) == 2


def test_cached_class_attributes():

    class X(object):

        def __init__(self, value):
            self.value = value

        @cached
        def x(self):
            return self.value

    x1 = X(1)
    x2 = X(2)
    x3 = X(3)

    assert x1.x() == 1
    assert x2.x() == 2
    assert x3.x() == 3



"""
def util_run_function_with_time(fn, args, kwargs):
    start_time = datetime.datetime.now()
    tmp = fn(*args, **kwargs)
    end_time = datetime.datetime.now()
    return (end_time - start_time), tmp
    
    
def test_performance():

    @cached
    def cached_fibonacci(x):
        if x == 0:
            return 0

        if x == 1:
            return 1

        return cached_fibonacci(x - 1) + cached_fibonacci(x - 2)

    def fibonacci(x):
        if x == 0:
            return 0

        if x == 1:
            return 1

        return fibonacci(x - 1) + fibonacci(x - 2)

    fib_value = 20
    cached_execution_time, cached_value = util_run_function_with_time(cached_fibonacci, (fib_value, ), {})
    uncached_execution_time, uncached_value = util_run_function_with_time(fibonacci, (fib_value, ), {})

    print(f" cached_execution_time: {cached_execution_time} - uncached_execution_time: {uncached_execution_time}")

    assert cached_execution_time < uncached_execution_time
    assert cached_value == uncached_value
"""
