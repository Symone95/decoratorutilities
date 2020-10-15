from functools import wraps

overload_handlers_map = {}
__all__ = ['overload']


def extract_signature_function(fn):
    """
    Funzione per l'estrazione della firma della funzione passata come parametro

    :param fn:
    :return:
    """

    if not fn.__annotations__:
        raise TypeError(f'Missing annotation for {fn.__qualname__}')

    return fn.__annotations__


def is_matching_signature(args_tuple, signature, handler) -> bool:
    """
    Funzione per il controllo del match tra gli args/kwargs e la funzione passati

    :param args_tuple: Tuple that contains *args and **kwargs
    :param signature: Signature of decorated function or class method
    :param handler: Execution of decorated function or class method
    :return: Return True if find signature in handlers_map else False
    """
    args, kwargs = args_tuple

    if len(args) + len(kwargs) != len(handler.__code__.co_varnames):
        return False

    if len(args):
        mod = handler.__qualname__.replace(f".{handler.__name__}", "")
        for value, (_key, _type) in zip(args, signature.items()):
            is_method = mod in value.__class__.__qualname__
            if not is_method:
                # Here is a function
                if not isinstance(value, _type):
                    return False
            else:
                # Here is a class method
                if not isinstance(args[1], _type):
                    return False

    if len(kwargs):
        for arg_name in kwargs:
            if arg_name not in signature:
                return False

            if not isinstance(kwargs[arg_name], signature[arg_name]):
                return False

    return True


def signature_already_exists(searching_signature, handlers_map):
    """
    Checking the existence of the function signature passed with those saved in the "handlers_map" map

    :param searching_signature:
    :param handlers_map:
    :return:
    """
    for (signature, handler) in handlers_map:
        if searching_signature == signature:
            return True

    return False


def overload(fn):
    """
    MODULE NAME
        overload

    MODULE REFERENCE
        https://decoratorutilities.readthedocs.io/en/latest/rst_templates/Decorators/overloading_decorator.html

    Decorate your own function or class method with **@overload** decorator to define multiple functions with same name but with different parameters

    :param fn: Decorated function or class method to overload
    :return: Return the execution of function or class method
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
