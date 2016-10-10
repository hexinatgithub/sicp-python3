def foo(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> foo(x)
    [0, 6, 20]
    """
    return [lst[i] * i for i in range(len(lst)) if i % 2 == 0]

# ----------------------------------------------------------------------

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be tree."
    return [root] + branches

def root(t):
    return t[0]

def branches(t):
    return t[1:]

def is_leaf(t):
    return not branches(t)

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True

# method
def square_tree(t):
    """Return a tree with the square of every element in t."""
    def square(x):
        return pow(x, 2)
    return tree(square(root(t)), [square_tree(branch) for branch in branches(t)])

def height(t):
    """Return height of a tree."""
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])

def tree_size(t):
    """Return the size of a tree."""
    if is_leaf(t):
        return 1
    else:
        return 1 + sum([tree_size(branch) for branch in branches(t)])

def tree_max(t):
    """Return the max of a tree"""
    if is_leaf(t):
        return root(t)
    else:
        return max([root(t)] + [tree_max(branch) for branch in branches(t)])

# ----------------------------------------------------------------------------------------------

# t = tree(1,
#          [tree(3,
#               [tree(4),
#                tree(5),
#                tree(6)]),
#           tree(2)])

# assert tree_max(t) == 6, "tree_max is wrong"
# assert tree_size(t) == 6, "tree_size is wrong"
# assert height(t) == 2, "tree_height is wrong"
# t2 = square_tree(t)
# assert tree_max(t2) == 36, "square_tree is wrong"

# ---------------------------------------------------------
def apply_to_all(fn, s):
    return [fn(x) for x in s]

def reduce(fn, s, init):
    reduced = init
    for x in s:
        reduced = fn(reduced, x)
    return reduced

from operator import add, mul
def eval_tree(tree):
    """Evaluates an expression tree with functions as root"""
    if is_leaf(tree):
        return root(tree)
    else:
        b_vals = apply_to_all(eval_tree, branches(tree))
        return reduce(root(tree), b_vals[1:], b_vals[0])

def hailstone_tree(n, h):
    if n % 2 == 0:
        even = n * 2
        return [n, hailstone_tree(even, h - 1)]
    else:
        even = n * 2
        odd = (n - 1) / 3 
        return [n, hailstone_tree(even, h - 1), hailstone_tree(odd, h - 1)]

def find_path(tree, x):
    if root(tree) == x:
        return root(tree)
    else:
        for branch in branches(tree):
            if find_path(branch, x) != None:    # find the element
                return [root(tree), find_path(branch, x)]
        # no such element
        return None