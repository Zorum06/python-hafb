#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


def modulus_four(n):
    r = n % 4
    if r == 0:
        print('Multiple of 4')
    elif r == 1:
        print('Remainder 1')
    elif r == 2:
        print('Remainder 2')
    elif r == 3:
        print('Remainder 3')
    else:
        assert False, 'This should not happen'


# --------------------------------------------------
def main():
    assert 5 > 2, 'hoopla'
    modulus_four(3)
    modulus_four(4)
    modulus_four(5)
    modulus_four(6)
    modulus_four(6/5)

# --------------------------------------------------
if __name__ == '__main__':
    main()
