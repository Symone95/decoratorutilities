import sys, os


def debug(fn):

    def wrapper(*args, **kwargs):

        try:
            return fn(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_next.tb_frame.f_code.co_filename)
            raise e(f"Found \"{exc_type}\" Exception in file \"{fname}\" on line \"{exc_tb.tb_next.tb_lineno}\""
                  f"\nError message: \"{e}\"")

    return wrapper
