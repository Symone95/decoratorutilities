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
    @mocking([
        ((7, 8, 9), {"c": 3}, 3)
    ])
    def a():
        pass

    @mocking([])
    def b():
        pass

    with pytest.raises(KeyError):
        a(1)

    with pytest.raises(KeyError):
        a(7, 8, 9, c=1)


def test_raise_missing_mocking_parameters():

    with pytest.raises(TypeError):
        @mocking([
            ((7, 8, 9), {"c": 3})
        ])
        def a():
            pass

    with pytest.raises(TypeError):
        @mocking([
            ({7, 8, 9}, {"c": 3})
        ])
        def a():
            pass
