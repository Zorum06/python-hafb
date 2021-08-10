#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""


def combine(size, color, animal):
    return f'{size}, {color}, {animal}'


# --------------------------------------------------
def main():
    """Make your noise here"""
    # map() is lazy it only produces the values as they are needed
    # ord is the unicode value
    m = map(ord, 'The purple Weber State')
    # print(list(m))
    print(next(m))
    print(next(m))
    print(next(m))
    print(next(m))

    print(list(map(ord, "The purple weber state")))

    for o in map(ord, 'The purple Weber State'):
        print(o)

    # multiple mapping
    sizes = ['small', 'medium', 'large']
    colors = ['green', 'blue', 'red']
    animals = ['penguin', 'llama', 'dog']

    # create a list of a map
    # note: Do not add the () to the function combine
    print(list(map(combine, sizes, colors, animals)))

    print([str(i) for i in range(5)])
    print(list(map(str, range(5))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
