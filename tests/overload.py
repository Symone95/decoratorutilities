import pytest
from typeguard import overload

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


def test_calling_missing_signature_method():

    @overload
    def a(a: int):
        return 0

    @overload
    def a(a: str):
        return 1

    with pytest.raises(TypeError):
        a([1])


def test_defining_same_signature_function():

    @overload
    def a(a: int):
        return 0

    with pytest.raises(NameError):
        @overload
        def a(a: int):
            return 0

def test_with_mixing_positions_name_param():

    def x(a: int, b: str, c: dict):
        return 1

    def x(a: int):
        return 1

    assert x(c={}, b='stringa', a=0) == 1
    # assert x(a=0, b='stringa', c={}) == 1
