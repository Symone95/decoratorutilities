import pytest

from typeguard import mocking


def test_mocking():

    @mocking([
        ((1, 2, 3), {"a": 1}, 1),
        ((4, 5, 6), {"b": 2}, 2)
    ])
    def a():
        pass

    assert a(1, 2, 3, a=1) == 1
    assert a(4, 5, 6, b=2) == 2


def test_raise_missing_mocking():

    @mocking([])
    def a():
        pass

    with pytest.raises(KeyError):
        a(1)
