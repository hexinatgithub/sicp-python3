from linkedList import *

def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == "len":
            return len_link(contents)
        elif message == "getitem":
            return getitem_link(contents, value)
        elif message == "push_first":
            contents = link(value, contents)
        elif message == "pop_first":
            f = first(contents)
            contents = rest(f)
            return f
        elif message == "str":
            return join_link(contents, " , ")
    return dispatch

def to_mutable_link(source):
    """Return a functional list with the same contents as source"""
    s = mutable_link()
    for element in reversed(source):
        s("push_first", element)
    return s

def dictionary():
    """Return a functional implementation of a dictionary"""
    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = join_link(non_matches, [key, value])
    def dispatch(message, key=None, value=None):
        if message == "getitem":
            return getitem(key)
        elif message == "setitem":
            setitem(key, value)
    return dispatch