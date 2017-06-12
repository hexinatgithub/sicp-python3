# Extra Questions

from lab11 import *

# Tree definition
class BinTree:
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left == self.empty and self.right == self.empty:
            return 'BinTree({})'.format(repr(self.label))
        left = 'BinTree.empty' if self.left == self.empty else repr(self.left)
        right = 'BinTree.empty' if self.right == self.empty else repr(self.right)
        return 'BinTree({}, {}, {})'.format(repr(self.label), left, right)

def binTree(tupleTree):
    """A convenience method for succinctly constructing binary trees.  The
    empty tuple or list stands for BinTree.empty; (V,) or [V] stands
    for BinTree(V); (V, T1, T2) or [V, T1, T2] stands for
    BinTree(V, binTree(T1), binTree(T2)).
    >>> binTree((3,
    ...          (1, (), [2]),
    ...          (6, [5], [7])))
    BinTree(3, BinTree(1, BinTree.empty, BinTree(2)), BinTree(6, BinTree(5), BinTree(7)))
    """
    if len(tupleTree) == 0:
        return BinTree.empty
    elif len(tupleTree) == 1:
        return BinTree(tupleTree[0])
    else:
        return BinTree(tupleTree[0], binTree(tupleTree[1]), binTree(tupleTree[2]))

def size(tree):
    """ Return the number of entries in the binary tree b.

    >>> b = BinTree(4,
    ...         BinTree(2,
    ...             BinTree(1)),
    ...         BinTree(6,
    ...             BinTree(5)))
    >>> size(b)
    5
    """
    "*** YOUR CODE HERE ***"

def contains(bst, elem):
    """
    >>> b = BinTree(5, BinTree(3, BinTree(2), BinTree(4)), BinTree(6))
    >>> contains(b, 5)
    True
    >>> contains(b, 6)
    True
    >>> contains(b, 7)
    False
    """
    "*** YOUR CODE HERE ***"

def unique(s):
    """Return a stream of the unique elements in s in the order that they
    first appear.

    >>> s = unique(lst_to_stream([1, 2, 2, 1, 0, 4, 2, 3, 1, 9, 0]))
    >>> s.first
    1
    >>> s.rest.first
    2
    >>> s.rest.rest.rest.rest.rest.first
    9
    """
    "*** YOUR CODE HERE ***"

def intersection(s1, s2):
    """Returns the intersection of two sets.

    >>> r = {0, 1, 4, 0}
    >>> s = {1, 2, 3, 4}
    >>> t = intersection(s, {3, 4, 2})
    >>> t
    {2, 3, 4}
    >>> intersection(r, t)
    {4}
    """
    "*** YOUR CODE HERE ***"

def union(s1, s2):
    """Returns the union of two sets.

    >>> r = {0, 6, 6}
    >>> s = {1, 2, 3, 4}
    >>> t = union(s, {1, 6})
    >>> t
    {1, 2, 3, 4, 6}
    >>> union(r, t)
    {0, 1, 2, 3, 4, 6}
    """
    "*** YOUR CODE HERE ***"
