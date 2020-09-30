from decoratorutilities import timeit
import time


@timeit
def hello():
    time.sleep(0.1)


if __name__ == "__main__":
    hello()
