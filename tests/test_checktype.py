import pytest
from decoratorutilities import checktype


def test_no_annotation():

    @checktype
    def a(a):
        return a

    assert a(1) == 1


def test_base_param():

    @checktype
    def a(a: int, b: int):
        return 1

    assert a(5, 6) == 1


def test_base_params():
    @checktype
    def a(a: int, b: int):
        return 1

    with pytest.raises(TypeError):
        a("invalid", "Invalid")

    with pytest.raises(TypeError):
        a("invalid", b="Invalid")

    with pytest.raises(TypeError):
        a(a="invalid", b="Invalid")



def test_pos_named_param():

    @checktype
    def a(a: str, b: int, c: list):
        return 1

    with pytest.raises(TypeError):
        a("Valid", 1, None)

    with pytest.raises(TypeError):
        a(a="Valid", b=1, c=None)

    assert a("Valid", 1, []) == 1
    assert a(a="Valid", b=1, c=[]) == 1
    assert a(c=[], b=1, a="Valid") == 1


def test_base_return():

    @checktype
    def a() -> int:
        return "Invalid"

    with pytest.raises(TypeError):
        a()


def test_valid_return():

    @checktype
    def a() -> int:
        return 0

    assert a() == 0

glob = 0

def test_unique_call():

    @checktype
    def a() -> int:
        global glob
        glob += 1
        return glob

    assert a() == 1
    assert a() == 2
