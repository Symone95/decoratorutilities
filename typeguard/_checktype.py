from functools import wraps

def checktype(fn):
    """
    Funzione per il controllo del tipo di dato passato come parametro e del return in base alla firma del metodo
    :param fn:
    :return:
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) > 0:
            for value, (_key, _type) in zip(args, fn.__annotations__.items()):
                if not isinstance(value, _type):
                    raise TypeError(f"Got: \'{value}\' of {type(value)} instance, expected {_type} instance for \"{_key}\" parameter")

        if len(kwargs) > 0:
            for kwarg in kwargs:
                if not isinstance(kwargs[kwarg], fn.__annotations__[kwarg]):
                    raise TypeError(f"Got: \'{kwargs[kwarg]}\' of {type(kwargs[kwarg])} instance, expected {fn.__annotations__[kwarg]} instance for \"{kwarg}\" parameter")

        fn_return = fn(*args, **kwargs)
        if "return" in fn.__annotations__ and not isinstance(fn_return, fn.__annotations__["return"]):
            raise TypeError(
                f"Got: \'{type(fn_return)}\' return type, expected {fn.__annotations__['return']} return type for \"{fn.__name__}\" function")

        return fn_return
    return wrapper
