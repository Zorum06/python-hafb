#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


store = []


def func1():
    x = 1
    y = 2
    return x + y


def func2():
    def local_func():
        a = 'hello'
        b = 'world'
        return a + b
    x = 1
    y = 2
    return x + y


def sort_by_last_letter(string):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(string, key=last_letter)


# local, enclosing, global, built-in
g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)
    inner()


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(func1())
    # print(func2())
    # s = ['xubair', 'hello', 'there', 'General', 'Kenobi', 'applea']
    # print(sort_by_last_letter(s))
    # print(store)
    outer()


# --------------------------------------------------
if __name__ == '__main__':
    main()
