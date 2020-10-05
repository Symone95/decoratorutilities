

def checkvalue(chekcs: dict):

    def fn_wrapper(fn):

        def args_wrapper(*args, **kwargs):
            return fn_wrapper(*args, **kwargs)

        return args_wrapper
    return fn_wrapper
