#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from pprint import pprint as pp


# --------------------------------------------------
def main():
    """Review Dictionaries"""
    urls = {'Google': "http://google.com",
            'Facebook': "http://Facebook.com",
            'Reddit': "https://Reddit.com"}
    print(type(urls))
    print(urls)
    urls['Reddit'] = 'http://reddit.com.temp'
    print(urls)
    urls['yahoo'] = 'http://yahoo.com'
    print(urls)
    # to iterate
    for values in urls.values():
        print(values)
    for items in urls.items():
        print(f'{items[0]}: {items[1]}')
    for key, value in urls.items():
        print(f'{key}: {value}')

    pp(urls)  # block
    # vs
    print(urls)  # inline


# --------------------------------------------------
if __name__ == '__main__':
    main()
