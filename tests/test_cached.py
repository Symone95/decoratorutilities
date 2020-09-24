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
