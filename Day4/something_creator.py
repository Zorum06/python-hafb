#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


class DecoratedClass:
    def __init__(self, original_func):
        self.original_function = original_func

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@DecoratedClass
def display():
    print(f'Display ran')


@DecoratedClass
def display_info(*args, **kwargs):
    print(f'Display ran with {args} and {kwargs}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    display()
    display_info('hello', 'there', general='Kenobi')


# --------------------------------------------------
if __name__ == '__main__':
    main()
