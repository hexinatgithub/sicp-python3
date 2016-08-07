"""Utilities for Maps"""

from math import sqrt
from random import sample

# Rename the built-in zip (http://docs.python.org/3/library/functions.html#zip)
_zip = zip

def map_and_filter(s, map_fn, filter_fn):
    """Return a new list containing the result of calling MAP_FUNC on each
    element of sequence S for which FILTER_FUNC returns a true value.

    >>> square = lambda x: x * x
    >>> is_odd = lambda x: x % 2 == 1
    >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)
    [1, 9, 25]
    """
    "*** YOUR CODE HERE ***"
    return [map_fn(x) for x in s if filter_fn(x)]

def key_of_min_value(d):
    """Returns the key in dict D that corresponds to the minimum value of D.

    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    "*** YOUR CODE HERE ***"
    return min(d, key=lambda key: d[key])

def zip(*sequences):
    """Returns a list of lists, where the i-th list contains the i-th
    element from each of the argument sequences.

    >>> zip(range(0, 3), range(3, 6))
    [[0, 3], [1, 4], [2, 5]]
    >>> for a, b in zip([1, 2, 3], [4, 5, 6]):
    ...     print(a, b)
    1 4
    2 5
    3 6
    >>> for triple in zip(['a', 'b', 'c'], [1, 2, 3], ['do', 're', 'mi']):
    ...     print(triple)
    ['a', 1, 'do']
    ['b', 2, 're']
    ['c', 3, 'mi']
    """
    return list(map(list, _zip(*sequences)))

def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and the
    i-th element of the sequence.


    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    return zip(range(start, start + len(s)), [x for x in s])

def distance(pos1, pos2):
    """Return the Euclidean distance between POS1 and POS2, which are pairs.

    >>> distance([1, 2], [4, 6])
    5.0
    """
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def mean(lst):
    """Return the arithmetic mean of a sequence of numbers.

    >>> mean([-1, 3])
    1.0
    >>> mean([0, -3, 2, -1])
    -0.5
    """
    assert len(lst) > 0, 'cannot find mean of empty sequence'
    return sum(lst) / len(lst)
