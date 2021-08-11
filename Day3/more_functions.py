#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""
import socket
from pprint import pp


class Resolver:
    def __init__(self):
        self.cache = {}

    def __call__(self, host):
        if host not in self.cache:
            self.cache[host] = socket.gethostbyname(host)
        return self.cache

    def clear(self):
        self.cache.clear()

    def has_host(self, host):
        return host in self.cache


def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


def test_lambda():
    names = ['Ricardo Hoopla', 'Ben Hur', 'Haden Chris', 'Liam Williamson']
    pp(sorted(names, key=lambda x: x.split()[-1]))


# --------------------------------------------------
def main():
    """Make your noise here"""
    # r = Resolver()
    # print(r)
    # print(r('weber.edu'))
    # print(r.__call__('weber.edu'))
    # print(r.has_host('weber.edu'))
    #
    # r.clear()
    # print(r.has_host('weber.edu'))
    #
    # # call the class
    # print(Resolver)
    # # call an instance
    # print(r)
    #
    # s = sequence_class(immutable=True)
    # t = s('Ogden')
    # print(t)
    # print(type(t))
    test_lambda()


# --------------------------------------------------
if __name__ == '__main__':
    main()
