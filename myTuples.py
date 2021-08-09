#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose: Review Tuples
"""

import argparse


def minMax(items):
    """
    Return the minimum and maximum of the collection
    :param items: collection of objects
    :return: min and max
    """
    return min(items), max(items)


# --------------------------------------------------
def main():
    """Make your noise here"""
    # a tuple of any kind of object
    t = "Ogden", 1.99, 2, 265e10
    print(t)
    print(t[1])
    print(t[2])
    print(f'The length of the tuple is {len(t)}')
    for item in t:
        print(f'item {item}')

    t2 = t*3
    for item in t2:
        print(f'Item {item}')

    # nested tuples
    a = (1, 2), (10, 20), (100, 200)
    for item in a:
        for innerItem in item:
            print(f'item {innerItem}')


# --------------------------------------------------


if __name__ == '__main__':
    # main()
    items = 2, 88, 11, 22, 90
    lower, upper = minMax(items)
    print(f'lower {lower} upper {upper}')
    # test for membership: in, not in
    print("I have 3 items") if 3 in items else print("I do not have 3 items")

