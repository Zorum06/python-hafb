#!/usr/bin/env python3
"""
Author: Ryan Williamson
Purpose: Say Hello to the world
"""


import argparse


def get_args():
    """
    Get the command-line arguments
    :return: list of parsed arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """
    This is where the actions is
    :return: None
    """
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
