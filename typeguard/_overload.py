from functools import wraps

overload_handlers_map = {}


def extract_signature_function(fn):
    if not fn.__annotations__:
        raise TypeError(f'Missing annotation for {fn.__qualname__}')

    return fn.__annotations__


def is_matching_signature(args_tuple, signature, handler) -> bool:
    args, kwargs = args_tuple

    if len(args) + len(kwargs) != len(handler.__code__.co_varnames):
        return False

    if len(args):
        for value, (_key, _type) in zip(args, signature.items()):
            if not isinstance(value, _type):
                return False

    if len(kwargs):
        for arg_name in kwargs:
            if arg_name not in signature:
                return False

            if not isinstance(kwargs[arg_name], signature[arg_name]):
                return False

    return True


def signature_already_exists(searching_signature, handlers_map):
    for (signature, handler) in handlers_map:
        if searching_signature == signature:
            return True

    return False


def overload(fn):
    """
    Funzione per poter eseguire l'overload di una funzione

    :param fn:
    :return:
    """
    fn_name = f"{fn.__module__}.{fn.__qualname__}"

    if fn_name not in overload_handlers_map:
        overload_handlers_map[fn_name] = []

    current_signature = extract_signature_function(fn)
    if signature_already_exists(current_signature, overload_handlers_map[fn_name]):
        raise NameError(f'Signature already exists for {fn.__qualname__}')

    overload_handlers_map[fn_name].append((current_signature, fn))

    @wraps(fn)
    def wrapper(*args, **kwargs):
        for (signature, handler) in overload_handlers_map[fn_name]:
            if is_matching_signature((args, kwargs), signature, handler):
                return handler(*args, **kwargs)
        else:
            raise ValueError(f'No matching signature for {fn.__qualname__} with arguments: {args} {kwargs}')

    return wrapper


__all__ = ['overload']
