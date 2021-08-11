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

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return iter(self.list)

    def __getitem__(self, item):
        result = self.list[item]
        return SortedSet(result).list if isinstance(item, slice) else result

    def __repr__(self):
        return f'SortedSet({repr(self.list) if self.list else ""})'

    def __eq__(self, rhs):
        """If not instance return NoImplemented
        rather than raise NoImplementedError"""
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self.list == rhs.list

    def __ne__(self, rhs):
        """If not instance return NoImplemented
        rather than raise NoImplementedError"""
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self.list != rhs.list


def main():
    """Make your noise here"""


# --------------------------------------------------
if __name__ == '__main__':
    main()
