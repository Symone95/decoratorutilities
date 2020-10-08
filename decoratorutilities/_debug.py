import sys
import os

"""import logging
import logging.config

logging.config.fileConfig('logging.conf')
#logging.basicConfig(filename='decoratorutilities.log', level=logging.DEBUG,
#                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger("decoratorutilities")"""


def module_fn_definition(fn) -> str:
    return f"{fn.__module__}.{fn.__name__}"


def parameters_fn_definition(*args, **kwargs) -> str:
    return ', '.join(
        [parameter_definition(key, arg) for key, arg in enumerate(args)] +
        [parameter_definition(name, kwarg) for name, kwarg in kwargs.items()]
    )


def parameter_definition(name, value) -> str:
    return f"{name}: {repr(value)} -> {type(value)}"


def debug(fn):
    """
    MODULE NAME
        debug

    MODULE REFERENCE
        https://decoratorutilities.readthedocs.io/en/latest/rst_templates/Decorators/debug_decorator.html

    Decorate your own function with **@debug** decorator to print in console more Exception details

    :param fn:
    :return:
    """
    # TODO: Far funzionare il logger
    from decoratorutilities import logger

    def wrapper(*args, **kwargs):

        base_string = f"{module_fn_definition(fn)}({parameters_fn_definition(*args, **kwargs)})"
        
        try:
            retr = fn(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()

            fname = "/".join(os.path.split(exc_tb.tb_next.tb_frame.f_code.co_filename))
            if fname.startswith(sys.path[0]):
                fname = fname.replace(sys.path[0], "")

            print(f"[{fname}:{exc_tb.tb_next.tb_lineno}]", base_string, "throws", parameter_definition("error", e))

            raise e
        else:
            print(base_string, parameter_definition("return", retr))
            return retr

    return wrapper
