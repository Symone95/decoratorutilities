import pytest
from decoratorutilities import cached


def test_no_annotation():

    """
    @cached
    def fun(p1: str):
        return p1
    """

    @cached
    def fun2(p2: str, p3: str):
        return p2

    #fun("ciao1")

    fun2("ciao2", "ciao3")
    fun2("ciao2", "ciao3")