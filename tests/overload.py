import pytest
from typeguard import overload

def test_base_overload():

    @overload
    def a(a: int) -> int:
        return 0

    @overload
    def a(a: str) -> str:
        return "hello, world!"

    assert a(1) == 0
    assert a("1") == "hello, world!"

