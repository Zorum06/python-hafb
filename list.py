#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def main():
    """Review lists"""
    l = [4, -2, 10, -10, 22, 55, 2, 77]
    print(l[2:6])
    print(f'len of list {len(l)}')
    print(f'last element {l[-1]}')
    # copy list (shallow: create another pointer to same data)
    t = l
    print(f'Is t the same as l? {t is l}')
    # to make a copy, generate a new list
    t = l.copy()  # this is faster
    # or t = l[:]
    print(f'Is t the same as l? {t is l}')
    print(f'Is t equivalent to l? {t == l}')



# --------------------------------------------------
if __name__ == '__main__':
    main()

