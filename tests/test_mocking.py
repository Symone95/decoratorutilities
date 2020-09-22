import pytest

from decoratorutilities import mocking


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


def test_mocking_wrong_argument_decorator():

    with pytest.raises(TypeError):
        @mocking({1, 2, 3, 4})
        def a():
            pass


def test_mocking_same_signature_different_return():

    with pytest.raises(KeyError):
        @mocking([
            ((1, 2, 3), {"a": 1}, 1),
            ((1, 2, 3), {"a": 1}, 2)
        ])
        def a():
            pass

