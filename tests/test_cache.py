import pytest
from decoratorutilities import cached


def test_cached_func():

    @cached
    def fun2(p2: str, p3: str):
        return p2

    fun2("ciao2", "ciao3")
    fun2("ciao2", "ciao3")
