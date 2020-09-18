import pytest
from typeguard import overload, checktype

# modulo # scope # nome funzione

def test_base_overload():

    @overload
    def a(a: int, b: str) -> int:
        return 0

    @overload
    def a(a: str) -> str:
        return "hello, world!"

    @overload
    def a() -> str:
        return "Senza params!"

    @overload
    def b(a: int) -> str:
        return "Funzione B!"

    @overload
    def b(a: str, b: int) -> int:
        return 5

    assert a(5, b="10") == 0
    assert a("1") == "hello, world!"
    assert a() == "Senza params!"
    assert b(0) == "Funzione B!"
    assert b("Ciao", 1) == 5


