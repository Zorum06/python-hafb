#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""


class SortedSet:
    def __init__(self, items=None):
        self.list = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self.list

    def __sizeof__(self):
        return len(self.list)

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return iter(self.list)

    def __getitem__(self, item):
        return self.list[item]


def main():
    """Make your noise here"""


# --------------------------------------------------
if __name__ == '__main__':
    main()
