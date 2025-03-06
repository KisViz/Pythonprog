#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import time


# Je, egy dekorator!
@contextmanager
def timed():
    start_time = time.time()
    yield #ez valasztja el a fuggvenyt
    #== ekotte __enter__ utana __exit__ resz
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))


def main():
    with timed():
        for i in range(100000):
            i = i * 6
        time.sleep(2)


if __name__ == '__main__':
    main()
