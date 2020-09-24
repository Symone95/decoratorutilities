from functools import wraps
from .utils import extract_signature_function, is_matching_signature, signature_already_exists

cache_handlers_map = {}


def cached(fn):
    """
    Funzione per poter cachare il ritorno di una funzione

    :param fn:
    :return:
    """
    fn_name = f"{fn.__module__}.{fn.__qualname__}"

    if fn_name not in cache_handlers_map:
        cache_handlers_map[fn_name] = []

    current_signature = extract_signature_function(fn)
    if signature_already_exists(current_signature, cache_handlers_map[fn_name]):
        raise NameError(f'Signature already exists for {fn.__qualname__}')

    cache_handlers_map[fn_name].append((current_signature, fn))

    @wraps(fn)
    def wrapper(*args, **kwargs):
        for (signature, handler) in cache_handlers_map[fn_name]:
            if is_matching_signature((args, kwargs), signature, handler):
                retr = handler(*args, **kwargs)

                if retr:
                    if "return" not in signature:
                        signature["return"] = retr

                    return signature["return"]
                else:
                    return retr
        else:
            raise ValueError(f'No matching signature for {fn.__qualname__} with arguments: {args} {kwargs}')

    return wrapper


__all__ = ['cached']
