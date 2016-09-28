## Lab 6: Trees and Mutable Sequences ##

# Sequences
def map(fn, seq):
    """Applies fn onto each element in seq and returns a list.

    >>> map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"

def filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2, 4]
    """
    "*** YOUR CODE HERE ***"

def reduce(combiner, seq):
    """Combines elements in seq using combiner.

    >>> reduce(lambda x, y: x + y, [1, 2, 3, 4])
    10
    >>> reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    >>> reduce(lambda x, y: x * y, [4])
    4
    """
    "*** YOUR CODE HERE ***"
