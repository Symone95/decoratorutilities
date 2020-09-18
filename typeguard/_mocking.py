from functools import wraps
from ._checktype import checktype


__all__ = ['mocking']

value_handler = []


@checktype
def save_mock(args: tuple, kwargs: dict, retr):
    mock = (args, kwargs, retr)
    if mock not in value_handler:
        value_handler.append(mock)
    else:
        raise KeyError(f"Parameters {mock} signature already exists")


def is_mock_matching(args_tuple, mocking_value_handler):
    args, kwargs = args_tuple

    for tuple_handler in mocking_value_handler:
        if args in tuple_handler and kwargs in tuple_handler:
            return tuple_handler
    return None


@checktype
def mocking(mocks: list):
    for mock in mocks:
        save_mock(*mock)

    def fn_wrapper(fn):

        @wraps(fn)
        def arg_wrapper(*args, **kwargs):
            args_tuple = is_mock_matching((args, kwargs), value_handler)
            if args_tuple:
                return args_tuple[2]
            else:
                raise KeyError("Unmatched parameters: ", (args, kwargs), " -> choose between: ", value_handler)

        return arg_wrapper

    return fn_wrapper
