#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):  # k stands for keyword argument. *tuple, **dict?
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


def print_pos_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


def colors(red, blue, green, **kwargs):
    print(f'r = {red}')
    print(f'b = {blue}')
    print(f'g = {green}')
    print(kwargs)


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print_args(1, 2, kwarg1='hello', kwarg2='there')
    # print_args(1, 2, 5, 6, kwarg1='hello', kwarg2='there')
    print_args(1, 2, 5, 6, kwarg1='hello', kwarg2='there', hoopla='dfs', hooplas='dfsdf')

    t = (11, 22, 33, 44, 55, 66)
    # *t unpacks the tuple (does not correspond to *args
    print_pos_args(*t)
    print()

    k = {'red': 21, 'blue': 120, 'green': 68, 'alpha': 52}
    colors(**k) # unpacking dictionary


# --------------------------------------------------
if __name__ == '__main__':
    main()
