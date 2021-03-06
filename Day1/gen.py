#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""
from math import sqrt


def take(count, iterable):
    """
    Take Items from the front of the iterable
    :param count: The maximum number of items to take
    :param iterable: the source
    :yield: at most 'count' items for 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        else:
            counter += 1
            yield item


def distinct(iterable):
    """
    Return unique items in list
    :param iterable: The source
    :yield: unique items in list
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def square_num(num):
    return sqrt(num) % 2 == 0


def run_distinct():
    items = [5, 5, 5, 7, 7, 2, 4, 6, 8]
    for item in distinct(items):
        print(item)
    print()
    distinct_list = set(items)
    print(distinct_list)


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(4, items):
        print(item)
    print()
    print(items[0:4])


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def capital_indexes(input):
    # capital_letters = []
    # for index, char in enumerate(input):
    #     if char.isupper():
    #         capital_letters.append(index)
    # return capital_letters
    return [i for i, char in enumerate(input) if char.isupper()]


def fib():
    prev = 0
    next_up = 1
    while True:
        my_sum = prev + next_up
        prev = next_up
        next_up = my_sum
        yield my_sum
        continue


def fibo():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append((sum(numbers)))
            numbers.pop(0)
        yield numbers[-1]
        continue


# --------------------------------------------------
def main():
    """Make your noise here"""
    # run_take()
    # run_distinct()
    # run_pipeline()
    # task: Create a list of the first 1 million square numbers
    n = 1000000
    # n_sq = (x*x for x in range(1, n + 1))  # saves memory uses generator
    # l_sq = list(n_sq)
    # l_sq = [(x * x for x in range(1, n + 1))]
    # print(f'Sum of first {n} numbers is {sum(l_sq)}')

    for i in range(100):
        print(next(fib()))
        i += 1


# --------------------------------------------------
if __name__ == '__main__':
    main()
