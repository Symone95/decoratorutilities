from functools import wraps
from .utils import extract_signature_function, is_matching_signature, signature_already_exists

overload_handlers_map = {}


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
