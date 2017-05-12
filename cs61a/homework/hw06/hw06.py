# Exceptions

# Avoiding key errors


def avoid_keyerror(dictionary, key):
    """ Returns the value associated with key in dictionary. If key 
    does not exist in the dictionary, print out 'Avoid Exception',
    insert KEY in the dictionary with value 'no value' and also return
    'no value'.

    >>> d = {1: 'one', 3: 'three', 5: 'five'}
    >>> avoid_keyerror(d, 3)
    'three'
    >>> avoid_keyerror(d, 4)
    Avoid Exception
    'no value'
    >>> d[4]
    'no value'
    >>> avoid_keyerror(d, 4)
    'no value'
    >>> avoid_keyerror(d, 3)
    'three'
    """
    try:
        return dictionary[key]
    except KeyError:
        print('Avoid Exception')
        dictionary[key] = 'no value'
        return dictionary[key]

# List replacement


class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __eq__(self, other):
        p = self
        while p is not Link.empty and other is not Link.empty:
            if other.first != p.first:
                return False
            p, other = p.rest, other.rest
        return p is Link.empty and other is Link.empty


def lst_replace_first_obvious(L, target, replacement):
    """Return the result of replacing the first occurrence of TARGET
    in linked-list L with REPLACEMENT.  Returns the original L unchanged
    if TARGET does not occur.  Non-destructive."""
    if L is Link.empty:
        return Link.empty
    elif L.first == target:
        return Link(replacement, L.rest)
    else:
        return Link(L.first, lst_replace_first_obvious(L.rest, target, replacement))


def lst_replace_first(L, target, replacement):
    """Return the result of replacing the first occurrence of TARGET
    in linked-list L with REPLACEMENT.  Returns the original L unchanged
    if TARGET does not occur.  Non-destructive.
    >>> L1 = Link(0, Link(2, Link(3, Link(2))))
    >>> lst_replace_first(L1, 2, 5)
    Link(0, Link(5, Link(3, Link(2))))
    >>> L1
    Link(0, Link(2, Link(3, Link(2))))
    >>> L2 = lst_replace_first(L1, 10, 5)
    >>> L2
    Link(0, Link(2, Link(3, Link(2))))
    >>> L2 is L1
    True
    """

    def lst_replace_first_exception(L, target, replacement):
        """Variant of lst_replace_first_obvious that raises exception if
        TARGET not present in L."""
        if L is Link.empty:
            raise ValueError
        elif L.first == target:
            return Link(replacement, L.rest)
        else:
            return Link(L.first, lst_replace_first_exception(L.rest, target, replacement))

    # Replace with apppropriate try block.
    try:
        return lst_replace_first_exception(L, target, replacement)
    except ValueError:
        return L

# Counting paths.


def num_paths(A, r, c, target):
    """Return the number of paths through list of same-length strings A
    that match TARGET, starting at A[R][C] and proceeding at each step
    one position north, south, east, west, northeast, northwest,
    southeast, or southwest.

    >>> num_paths([ "AB", "BC" ], 0, 0, "ABBC")
    2
    >>> num_paths([ "CBB", "BBA" ], 0, 1, "BBCBBA")
    12
    >>> long = "A" * 10 + "B" * 10
    >>> num_paths([long] * 2, 0, 5, long)
    82373282112
    """
    if target == "":
        return 1
    M = len(A)              # Number of rows
    N = M and len(A[0])     # Number of columns, 0 if A is empty
    S = len(target)

    memo = _________________________________  # REPLACE

    def count(r, c, k):
        """The number of paths through A starting at R, C that match
        TARGET[k:]."""
        if 0 <= r < M and 0 <= c < N:
            if A[r][c] == target[k]:
                "*** YOUR CODE HERE ***"
            else:
                return 0
        else:
            return 0

    def memoized_count(r1, c1, k1):
        "*** YOUR CODE HERE ***"

    r = count(r, c, 0)
    return r
