#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""

from functools import reduce
import operator
from pprint import pp


def count_words(doc):
    """
    Counts words in a document and produces a dictionary mapping words
    """
    # normalize the string
    normalize_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalize_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def combine_counts(d1, d2):
    """
    Combine two dictionaries
    """
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


def main():
    """Make your noise here"""
    numbers = [-7, 2, 5, 8, -1, 90, -2, -33, 0, 12]
    print([x for x in numbers if x > 0])
    # positives = list(filter(lambda x: x > 0, numbers))
    # print(list(filter(None, numbers)))

    # a + b = operator.add(a, b)
    accumulator = operator.add(numbers[0], numbers[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    print(accumulator)

    # use reduce
    numbers = []
    print(reduce(operator.add, numbers, 0))

    print(count_words('Oh Baby Yeah!'))
    documents = ['It was the best of times, it was the worst of times',
                 'I went to the woods because I wished to live deliberately, to front only the essentials',
                 'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him'
                 'I do not like green eggs and ham. I do not like them Sam-I-Am']
    counts = map(count_words, documents)
    total_counts = reduce(combine_counts, counts)
    pp(total_counts)


# --------------------------------------------------
if __name__ == '__main__':
    main()
