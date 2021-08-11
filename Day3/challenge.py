#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


def online_count(dict):
    return len([s for s in dict.values() if s == 'online'])


# --------------------------------------------------
def main():
    """Make your noise here"""
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    print(online_count(statuses))


# --------------------------------------------------
if __name__ == '__main__':
    main()
