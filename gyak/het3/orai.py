class swallow_exceptions():
    def __init__(self, err):
        pass
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type.__name__, "elnyelve")
        return True

with swallow_exceptions([ZeroDivisionError]):
    1 / 0

with swallow_exceptions([ValueError]):
    int("asd")

print("----------------------------------------------------")

import datetime
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(datetime.datetime.now())
        print(func.__name__, args, kwargs)
        try:
            vege = func(*args, **kwargs)
            print("visszateresi ertek: ", vege)
            return vege
        except Exception as e:
            print("raised:",e)

    return wrapper



@debug
def division(n):
    return n / 0

@debug
def another_division(n):
    return n / 2

another_division(10)
print("--------")
division(10)

print("----------------------------------------------------")

from contextlib import contextmanager
import time


@contextmanager
def timed():
    start_time = time.time()
    yield
    end_time = time.time()
    print("Total execution time: {}".format(end_time-start_time))


def cached(func):
    dikt = {}
    @wraps(func)
    def wrapper(*args, **kwargs):

        if args in dikt:
            return dikt[args]
        else:
            dikt[args] = func(*args, **kwargs)
            return dikt[args]
    return wrapper


@cached
def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


def main():
    with timed():
        for i in range(5000):
            factorial(3000 + (i % 50))

if __name__ == '__main__':
    main()

print("----------------------------------------------------")

def deprecated(fn):
    elozo = ""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal elozo #emiatt tudjuk elerni a kuso valtozot
        if elozo != fn.__name__:
            print(f"The called function '{fn.__name__}' is deprecated.")
            elozo = fn.__name__

    return wrapper

@deprecated
def barmi():
    pass

barmi()
barmi()
barmi()
barmi()

print("----------------------------------------------------")

def flatten(*args):
    for elem in args:
        for i in elem:
            yield i

for i in flatten(range(3), range(3, 5), ["cica", "korte", "kiwi"]):
    print(i, end=" ")

















