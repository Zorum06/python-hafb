#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

from itertools import islice, count
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
    """Make your noise here"""
    # thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    # print(list(thousand_primes))

    # use the built-ins any, all
    # print(any([False, False, True]))
    # print(all([False, False, True]))
    cities = ['London', 'Madrid', 'New York', 'Ogden']
    # task check all members in the collection have uppercase for first letter
    print(all(city[0].isupper() for city in cities))
    print(all(city == city.title() for city in cities))

    # use built in zip
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20, 21, 22, 22, 21, 19, 18, 16]
    tuesday = [12, 13, 14, 16, 20, 20, 21, 20, 19, 16, 14, 12]

    # for item in zip(sunday, monday):
    #     print(item)
    for sun, mon in zip(sunday, monday):
        print(f'Average {(sun + mon) / 2.0}')

    for temp in zip(sunday, monday, tuesday):
        print(f'min = {min(temp)} max = {max(temp)} and avg {sum(temp)/len(temp):4.1f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
