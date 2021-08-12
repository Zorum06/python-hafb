#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/12/2021
Purpose:
"""

import time


message = 'global'


def make_timer():
    last_call = None

    def elapsed():
        nonlocal last_call
        now = time.time()
        if last_call is None:
            last_call = now
            return None
        result = now - last_call
        last_call = now
        return result
    return elapsed



def enclosing():
    message = 'enclosing'

    def local():
        # global message # bring global into scope
        nonlocal message # bring enclosing into scope
        message = 'local'

    print(f'enclosing message {message}')
    local()
    print(f'enclosing message {message}')


# --------------------------------------------------
def main():
    """Make your noise here"""
    # print(f'global message {message}')
    # enclosing()
    # print(f'global message {message}')
    t = make_timer()
    print(t())
    print(t())
    time.sleep(2)
    print(t())
    print(t())


# --------------------------------------------------
if __name__ == '__main__':
    main()
