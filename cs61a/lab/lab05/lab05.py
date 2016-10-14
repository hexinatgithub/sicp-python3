## Trees, Dictionaries ##

#########
# Trees #
#########

import inspect
# Tree definition - same Data Abstraction but different implementation from lecture
def tree(root, branches=[]):
    #for branch in branches:
    # assert is_tree(branch)
    return lambda dispatch: root if dispatch == 'root' else list(branches)

def root(tree):
    return tree('root')

def branches(tree):
    return tree('branches')

def is_tree(tree):
    try:
        tree_data = inspect.getargspec(tree)
        assert tree_data == inspect.getargspec(lambda dispatch: None)
        return all([is_tree(branch) for branch in branches(tree)])
    except:
        return False

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])


# Q1
def countdown_tree():
    """Return a tree that has the following structure.

    >>> print_tree(countdown_tree())
    10
      9
        8
      7
        6
          5
    """
    return tree(10, [tree(9, 
                            [tree(8)]),
                     tree(7, 
                            [tree(6, 
                                     [tree(5)])])]
           )

# Q2
def size_of_tree(t):
    """Return the number of entries in the tree.

    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> size_of_tree(numbers)
    7
    """
    if is_leaf(t):
        return 1
    size = 1
    for branch in branches(t):
        size = size + size_of_tree(branch)
    return size

################
# Dictionaries #
################

# Q3
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    dic = {}
    for word in word_list:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
    return dic

