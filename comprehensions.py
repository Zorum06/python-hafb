#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from math import sqrt


def is_prime(x):
    """
    Returns true or false if value is prime
    :param x: input
    :return: true or false
    """

    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# --------------------------------------------------
def main():
    """comprehensions"""
    words = 'Today I am very happy because I have a switch to pass the time'.split()
    print(words)
    lwords = []
    for word in words:
        lwords.append(len(word))
    print(lwords)

    # list comprehension
    totals = [len(word) for word in words]
    print(totals)

    prime_nums = [x for x in range(1001) if is_prime(x)]
    print(prime_nums)
    print(len(prime_nums))


# --------------------------------------------------
if __name__ == '__main__':
    main()
