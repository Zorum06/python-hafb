#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


def is_even(num):
    return num % 2 == 0

class CallMe:
    def __call__(self):
        print('called')


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(callable(is_even))
    is_odd = lambda x: x % 2 == 1
    print(callable(is_odd))
    print(callable(list))
    print(callable(CallMe))




# --------------------------------------------------
if __name__ == '__main__':
    main()
