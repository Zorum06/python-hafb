#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fname',
                        metavar='str',
                        help='A file to read')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    str_arg = args.arg

    print(f'str_arg = "{str_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
