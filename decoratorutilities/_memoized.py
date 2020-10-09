from functools import wraps

memoized_value_handlers_map = {}
__all__ = ['memoized']


def get_value_matching(memoized_value_handlers_map, args_tuple):
    args, kwargs = args_tuple
    for value_handler in memoized_value_handlers_map:
        if args == value_handler["args"] and kwargs == value_handler["kwargs"]:
            return value_handler
    return None


def memoized(fn):
    """
    MODULE NAME
        memoized

    MODULE REFERENCE
        https://decoratorutilities.readthedocs.io/en/latest/rst_templates/Decorators/memoized_decorator.html

    Decorate your own function or class method with **@memoized** decorator to speed up it by storing the results and returning the cached result when the same inputs occur again

    :param fn: Instance of decorated function or class method
    :return: Return the execution of decorated function or class method
    """
    fn_name = f"{fn.__module__}.{fn.__qualname__}"

    if fn_name not in memoized_value_handlers_map:
        memoized_value_handlers_map[fn_name] = []

    @wraps(fn)
    def wrapper(*args, **kwargs):

        check = get_value_matching(memoized_value_handlers_map[fn_name], (args, kwargs))
        if not check:
            tmp = fn(*args, **kwargs)
            memoized_value_handlers_map[fn_name].append({"args": args, "kwargs": kwargs, "return": tmp})
            return tmp
        else:
            return check["return"]

    return wrapper
