#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""


def outer_function(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


def decorator(func):
    def wrapper(*args):
        print(f'wrapper executed this before {func.__name__}')
        return func(*args)
    return wrapper


@decorator
def display():
    print(f'Display function ran')


# this will not work with the current decorator
# unless you make sure pass all the parameters
@decorator
def display_info(name, age):
    print(f'Display function ran {name} {age}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    # f = outer_function('hello')
    # f2 = outer_function('there')
    # f()
    # f2()
    #
    # decorator_display = decorator(display)
    display()
    display_info('Ryan', '30')


# --------------------------------------------------
if __name__ == '__main__':
    main()
