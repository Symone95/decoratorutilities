from functools import wraps

cached_value_handlers_map = {}


def get_value_matching(cached_value_handlers_map, args_tuple):
    args, kwargs = args_tuple
    for value_handler in cached_value_handlers_map:
        if args == value_handler["args"] and kwargs == value_handler["kwargs"]:
            return value_handler
    return None


def cached(fn):
    """
    Funzione per poter cachare il ritorno di una funzione

    :param fn:
    :return:
    """
    fn_name = f"{fn.__module__}.{fn.__qualname__}"

    if fn_name not in cached_value_handlers_map:
        cached_value_handlers_map[fn_name] = []

    @wraps(fn)
    def wrapper(*args, **kwargs):

        check = get_value_matching(cached_value_handlers_map[fn_name], (args, kwargs))
        if not check:
            tmp = fn(*args, **kwargs)
            cached_value_handlers_map[fn_name].append({"args": args, "kwargs": kwargs, "return": tmp})
            return tmp
        else:
            return check["return"]

    return wrapper


__all__ = ['cached']
