#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


# --------------------------------------------------
def main():
    """Make your noise here"""
    square = raise_to(2)
    print(square(5))
    print(square(9))
    print(square.__closure__)

    cube = raise_to(3)
    print(cube.__closure__)
    print(cube(5))
    print(cube(10))


# --------------------------------------------------
if __name__ == '__main__':
    main()
