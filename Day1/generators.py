#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


def gen_values(iterable):
    iterator = iter(iterable)
    for i in range(4):
        yield next(iterator)


def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('iterable is empty')


# --------------------------------------------------
def main():
    """Review iterators and generators"""
    iterable = ['Spring', 'Summer', 'Fall', 'Winter']
    iterator = iter(iterable)
    print(type(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print()

    print(first(iterable))
    print()

    for item in gen_values(iterable):
        print(item)

    for item in gen246():
        print(item)


# --------------------------------------------------
if __name__ == '__main__':
    main()
