from functools import wraps
from ._checktype import checktype

value_handler = []


@checktype
def check_mock(args: tuple, kwargs: dict, retr):
    return


def save_mock(mock: tuple):
    if mock not in value_handler:
        value_handler.append(mock)
    else:
        raise KeyError(f"Tuple {mock} added yet")


def is_mock_matching(args_tuple, value_handler): #, current_tuple):
    args, kwargs = args_tuple
    #print("args: ", args, " - KWARGS: ", kwargs)
    for tuple_handler in value_handler:
        #print("CHECK: ", tuple_handler)
        if args in tuple_handler and kwargs in tuple_handler:
            #print("TUPLA TROVATA: ", tuple_handler)
            return tuple_handler
    return None


def mocking(mocks: list):
    # Controllo la validità della tupla inserita come parametro
    for mock in mocks:
        check_mock(*mock)
        # Salvo nella lista le tuple passate
        save_mock(mock)

    def fn_wrapper(fn):

        @wraps(fn)
        def arg_wrapper(*args, **kwargs):
            print("value_handler: ", value_handler)

            tuple = is_mock_matching((args, kwargs), value_handler)
            if tuple:
                return tuple[2]
            else:
                raise KeyError("Unmatched parameters: ", (args, kwargs), " -> choose between: ", value_handler)

        return arg_wrapper

    return fn_wrapper
