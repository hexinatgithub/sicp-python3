# Iterators

class Letters(object):

    def __init__(self, start, finish):
        self.current = start
        self.finish = finish

    def __next__(self):
        if self.current > self.finish:
            raise StopIteration
        result = self.current
        self.current = chr(ord(result)+1)
        return result

    def __iter__(self):
        return self

def for_each(sequence, function):
    """Apply function to each element of a sequence."""
    iterator = sequence.__iter__()
    try:
        while True :
            element = iterator.__next__()
            function(element)
    except StopIteration:
        pass
		
# Generator functions

def letters(start, finish):
    """Return a generator over letters."""
    current = start
    while current <= finish:
        yield current
        current = chr(ord(current)+1)

# Streams

class Stream(object):
    """A lazily computed recursive list."""

    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

empty_stream = Stream.empty

def make_const_stream(x):
    """An infinite stream of X's."""
    return Stream(x, lambda: make_const_stream(x))

def make_integer_stream(first=1):
    """Return an infinite stream of increasing integers.

    >>> from operator import add
    >>> stream_to_list(make_integer_stream(1), 5)
    [1, 2, 3, 4, 5]
    """
    return Stream(first, lambda: make_integer_stream(first+1))

# Stream manipulation

def map_stream(fn, s):
    """Return a stream of the values of fn applied to the elements of stream s.

    >>> s = make_integer_stream(3)
    >>> stream_to_list(truncate_stream(map_stream(lambda x: x*x, s), 4))
    [9, 16, 25, 36]
    """
    if s is Stream.empty:
        return s
    return Stream(fn(s.first), lambda: map_stream(fn, s.rest))

def filter_stream(fn, s):
    """Return a stream of the elements of s for which fn is true."""
    if s is Stream.empty:
        return s
    if fn(s.first):
        return Stream(s.first, lambda: filter_stream(fn, s.rest))
    return filter_stream(fn, s.rest)

def reduce_stream(fn, s, n):
    """Accumulate the elements of s using two-argument fn, starting with n."""
    if s is Stream.empty:
        return n
    return reduce_stream(fn, s.rest, fn(n, s.first))

def truncate_stream(s, k):
    """Return a stream over the first k elements of stream s."""
    if s is Stream.empty or k == 0:
        return empty_stream
    def compute_rest():
        return truncate_stream(s.rest, k-1)
    return Stream(s.first,
                  lambda: truncate_stream(s.rest, k-1))

def stream_to_list(s, n=10):
    """A list containing the elements of stream S,
    up to a maximum of N."""
    r = []
    while n > 0 and s is not Stream.empty:
        r.append(s.first)
        s = s.rest
        n -= 1
    return r

def combine_streams(f, s0, s1):
    """Return a stream of the elements of S0 and S1 combined in pairs with
    two-argument function F."""
    def compute_rest():
        return combine_streams(f, s0.rest, s1.rest)
    if s0 is Stream.empty:
        return s0
    elif s1 is Stream.empty:
        return s1
    else:
        return Stream(f(s0.first, s1.first),
                      lambda: combine_streams(f, s0.rest, s1.rest))

from operator import add
    
def add_streams(s0, s1):
    """The stream of sums of corresponding elements of S0 and S1.
    >>> S0 = Stream(1, lambda: Stream(2, lambda: Stream(3)))
    >>> S1 = Stream(8, lambda: Stream(9, lambda: Stream(10)))
    >>> stream_to_list(add_streams(S0, S1), 10)
    [9, 11, 13]
    """
    return combine_streams(add, s0, s1)

# Iterators and streams

def iterator_to_stream(iterator):
    """Return a stream over the elements of an iterator."""
    def compute_rest():
        try:
            first = iterator.__next__()
            return Stream(first, compute_rest)
        except:
            return empty_stream
    return compute_rest()
            
def positives():
    """Return a generator over positive integers."""
    i = 1
    while True:
        yield i
        i += 1

# Streams example

def primes(pos_stream):
    """Return a stream of primes.
    
    pos_stream -- a stream of positive integers, starting with 2.

    >>> p1 = primes(make_integer_stream(2))
    >>> stream_to_list(p1, 7)
    [2, 3, 5, 7, 11, 13, 17]
    >>> p2 = primes(iterator_to_stream(positives()).rest)
    >>> stream_to_list(p2, 7)
    [2, 3, 5, 7, 11, 13, 17]
    """
    def not_divisible(x):
        return x % pos_stream.first != 0
    def compute_rest():
        return primes(filter_stream(not_divisible, pos_stream.rest))
    return Stream(pos_stream.first, compute_rest)
