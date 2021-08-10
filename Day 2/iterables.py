#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/10/2021
Purpose: cover comprehensions and iterables
"""


# --------------------------------------------------
def main():
    """Make your noise here"""
    # list comprehensions: [expression(item)] for item in iterable
    # set comprehension: {expression)item) for item iterable
    s = {i for i in range(10)}
    print(s)
    # dict comprehension: {key_expression: value_expression for item in iterable}
    d = {i: i*2 for i in range(10)}
    print(d)
    # generator comprehensions (item for item in iterable)
    g = (i for i in range(10))
    print(g)

    # multiple if clauses
    points = []
    for x in range(5):
        for y in range(3):
            points.append((x, y))
    print(points)

    points = [(x, y) for x in range(5) for y in range(3)]
    print(points)

    # version 1 loops
    # values = []
    # for x in range(100):
    #     if x > 50:
    #         for y in range(100):
    #             if x - y != 0:
    #                 values.append(x/(x-y))
    # print(values)
    #
    # # version 2 comprehension
    # values = [(x/(x-y))
    #           for x in range(100) if x > 50
    #           for y in range(100) if x-y != 0]
    # print(values)
    print()

    # task
    outer = []
    for x in range(10):
        inner = []
        for y in range(x):
            inner.append(y*3)
        outer.append(inner)
    print(outer)

    outer = [[y*3 for y in range(x)] for x in range(10)]
    print(outer)
    print()

    g = ((x, y) for x in range(5) for y in range(5))
    print(list(g))
    l = [(x, y) for x in range(5) for y in range(5)]
    print(l)

    s = set([2, 4, 6, 6, 8])
    print(s)

    s = {2, 4, 5, 5, 6}
    print(s)


# --------------------------------------------------
if __name__ == '__main__':
    main()
