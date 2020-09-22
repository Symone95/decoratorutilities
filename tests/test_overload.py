import pytest
from decoratorutilities import overload

# modulo # scope # nome funzione


def test_with_mixing_positions_name_param():

    @overload
    def x(a: int, b: str, c: dict):
        return 1

    @overload
    def x(a: int):
        return 2

    assert x(c={}, b='stringa', a=0) == 1
    assert x(a=0, b='stringa', c={}) == 1
    assert x(0, 'stringa', {}) == 1

    assert x(1) == 2
    assert x(a=3) == 2


def test_with_missing_type():

    with pytest.raises(TypeError):
        @overload
        def x(a):
            pass


def test_partial_overload_types():

    @overload
    def a(a:int, b):
        return 1

    @overload
    def a(a:str, b):
        return 2

    assert a(1, None) == 1
    assert a('1', None) == 2


def test_calling_no_matching_signature():

    @overload
    def a(a: int):
        return 1

    with pytest.raises(ValueError):
        a('string')


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

    with pytest.raises(ValueError):
        assert a([1]) is None


def test_defining_same_signature_function():

    @overload
    def a(a: int):
        return 0

    with pytest.raises(NameError):
        @overload
        def a(a: int):
            return 0

