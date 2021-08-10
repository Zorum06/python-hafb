#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

import math


class Point:
    def __init__(self, x=0, y=0):
        """Initializes the position of a new point"""
        self.x = x
        self.y = y

    def reset(self):
        """Rests point to 0, 0"""
        self.move(0, 0)

    def move(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.hypot(other_point.x - self.x, other_point.y - self.y)


# --------------------------------------------------
def main():
    """Make your noise here"""
    p1 = Point()
    p2 = Point()
    p1.x = 5
    p1.y = 4
    p2.x = 3
    p2.y = 9
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    p2.reset()
    print(p2.x, p2.y)
    p2.move(5, 2)
    print(p2.x, p2.y)
    p3 = Point(y=9, x=12)
    print(p3.x, p3.y)
    print(p3.calculate_distance(p1))
    assert(p2.calculate_distance(p1) == p1.calculate_distance(p2))


# --------------------------------------------------
if __name__ == '__main__':
    main()
