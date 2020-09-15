import pytest
from typeguard import checktype


# Guardare anche la libreria typing

def test_base_param():

    @checktype
    def a(b: int):
        print("CHIAMO LA FUNC")
        return 1

    # E' il try/except di pytest
    with pytest.raises(TypeError):
        print("SONO QUA 1")
        a("Invalid")

    assert a(5) == 1
    #assert a("r") == "TypeError(\"got: 'r' of <class 'str'> instance, expected <class 'str'> instance for \"b\" parameter\")"


"""
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

"""