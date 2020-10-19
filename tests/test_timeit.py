from decoratorutilities import timeit
import time


@timeit
def test_hello():
    time.sleep(0.1)
    print("PASSED")
