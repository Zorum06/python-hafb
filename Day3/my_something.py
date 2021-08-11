#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


import math
import traceback


def inclination(dx, dy):
    if dx == 0 or dy == 0:
        raise InclinationError('Illegal input values')
    return math.degrees(math.atan(dy/dx))


class InclinationError(Exception):
    pass


# --------------------------------------------------
def main():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)
        traceback.print_tb(e.__traceback__)
        s = traceback.format_tb(e.__traceback__)
        print(s)


# --------------------------------------------------
if __name__ == '__main__':
    main()
