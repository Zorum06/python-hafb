#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def main():
    """Make your noise here"""
    r = range(5)
    print(type(r))
    for item in r:
        print(item)
    # set upper and lower limit
    r = range(5, 10)
    for item in r:
        print(item)

    # create list out of ranges
    l = list(range(50, 55))
    print(type(l))
    for item in l:
        print(item)

    # ranges thir parameter is the step size
    l = list(range(2, 12, 2)) + list(range(20, 60, 3))
    print(type(l))
    for item in l:
        print(item)

    # enumerate
    t = [6, 365, 67, 1, 99, 234]
    for i, v in enumerate(t):
        print(f'Index {i}, value {v}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

