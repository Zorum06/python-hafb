#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('item',
                        help='item(s) to bring',
                        metavar='str',
                        nargs='+',  # one or more arguments
                        )

    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    items = list(args.item)
    length = len(items)
    bringing = ''
    if args.sorted:
        items.sort()

    # 1 item just print item
    if length == 1:
        bringing = items[0]

    # 2 items, item1 and item2
    elif length == 2:
        bringing = ' and '.join(items)

    # 3 or more items, item1, item2, itemX and itemLast
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
