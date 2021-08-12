#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


def enclosing():
    x = 'close over'

    def local_func():
        print(x)
    return local_func


def test_enclosing():
    lf = enclosing()
    lf()
    print(lf.__closure__)


# --------------------------------------------------
def main():
    """Make your noise here"""
    test_enclosing()


# --------------------------------------------------
if __name__ == '__main__':
    main()
