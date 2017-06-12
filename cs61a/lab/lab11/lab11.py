class Stream:
    """A lazily computed linked list."""

    class empty:
        """The empty stream."""
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    # As a convenience, we allow the second arguemt to Stream to be
    # another Stream (without having to have a lambda: in front.)

    def __init__(self, first, compute_rest=empty):
        """A stream whose first element is FIRST and whose tail is either
        a stream or stream-returning parameterless function COMPUTE_REST."""
        self.first = first
        if compute_rest is Stream.empty or isinstance(compute_rest, Stream):
            self._rest, self._compute_rest = compute_rest, None
        else:
            assert callable(compute_rest), 'compute_rest must be callable.'
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

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def make_fib_stream():
    """Return a stream containing the Fib sequence.

    >>> fib = make_fib_stream()
    >>> fib.first
    0
    >>> fib.rest.first
    1
    >>> fib.rest.rest.rest.rest.first
    3
    """
    return fib_stream_generator(0, 1)

def fib_stream_generator(a, b):
    def compute_rest():
        return fib_stream_generator(b, a + b)
    return Stream(a, compute_rest)

def lst_to_stream(lst):
    if not lst:
        return Stream.empty
    return Stream(lst[0], lambda: lst_to_stream(lst[1:]))

def interleave(stream1, stream2):
    """Return a stream with alternating values from stream1 and stream2.

    >>> ints = make_integer_stream(1)
    >>> fib = make_fib_stream()
    >>> alternating = interleave(ints, fib)
    >>> alternating.first
    1
    >>> alternating.rest.first
    0
    >>> alternating.rest.rest.first
    2
    >>> alternating.rest.rest.rest.first
    1
    """
    if stream1 is Stream.empty:
        return stream2
    elif stream2 is Stream.empty:
        return stream1
    else:
        return Stream(stream1.first, lambda: interleave(stream2, stream1.rest))

def add_streams(s1, s2):
    """Returns a stream that is the sum of s1 and s2.

    >>> stream1 = make_integer_stream()
    >>> stream2 = make_integer_stream(9)
    >>> added = add_streams(stream1, stream2)
    >>> added.first
    10
    >>> added.rest.first
    12
    >>> added.rest.rest.first
    14
    """
    if s1 is Stream.empty:
        return s2
    elif s2 is Stream.empty:
        return s1
    else:
        return Stream(s1.first + s2.first, lambda: add_streams(s1.rest, s2.rest))

def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    >>> find_duplicates(list(range(100000)) + [-1]) # make sure you have linear time
    False
    """
    return len(set(lst)) != len(lst)
