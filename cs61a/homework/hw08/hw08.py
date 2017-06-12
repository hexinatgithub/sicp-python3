import time


def timeit(func):
    """Returns the time required to execute FUNC() in seconds."""
    t0 = time.perf_counter()
    func()
    return time.perf_counter() - t0


def missing_val(lst0, lst1):
    """Assuming that lst0 contains all the values in lst1, but lst1 is missing
    one value in lst0, return the missing value.  The values need not be
    numbers.

    >>> from random import shuffle
    >>> missing_val(range(10), [1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> big0 = [str(k) for k in range(15000)]
    >>> big1 = [str(k) for k in range(15000) if k != 293 ]
    >>> shuffle(big0)
    >>> shuffle(big1)
    >>> missing_val(big0, big1)
    '293'
    >>> timeit(lambda: missing_val(big0, big1)) < 1.0
    True
    """
    a = set(lst0)
    b = set(lst1)
    return (a - b).pop()


def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    >>> find_duplicates_k(4, [1, 1, 2, 3, 3])
    True
    """
    lst = lst[:k+1]
    s = set(lst)
    return len(s) != len(lst)

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


def constant_stream(x):
    """The infinite stream all of whose values are X."""
    result = Stream(x, lambda: result)
    return result


def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first + 1)
    return Stream(first, compute_rest)


def stream_to_list(s, n=10):
    """A list containing the elements of stream S,
    up to a maximum of N."""
    r = []
    while n > 0 and s is not Stream.empty:
        r.append(s.first)
        s = s.rest
        n -= 1
    return r


def map_stream(fn, s):
    if s is Stream.empty:
        return s
    return Stream(fn(s.first), lambda: map_stream(fn, s.rest))


def combine_streams(fn, a, b):
    """The stream consisting of FN(a1, b1), FN(a2, b2), ..., where
    ai and bi are elements of streams A and B, respectively, and FN
    is a two-parameter function.  The stream terminates when either of
    A or B terminates."""
    if a is Stream.empty or b is Stream.empty:
        return Stream.empty
    else:
        return Stream(fn(a.first, b.first),
                      lambda: combine_streams(fn, a.rest, b.rest))


def scale_stream(s, k):
    """Return a stream of the elements of S scaled by a number K.

    >>> ints = make_integer_stream(1)
    >>> s = scale_stream(ints, 5)
    >>> stream_to_list(s, 5)
    [5, 10, 15, 20, 25]
    >>> s = scale_stream(Stream("x", lambda: Stream("y")), 3)
    >>> stream_to_list(s)
    ['xxx', 'yyy']
    >>> stream_to_list(scale_stream(Stream.empty, 10))
    []
    """
    if s is Stream.empty:
        return s
    else:
        return Stream(s.first * k,
                      lambda: scale_stream(s.rest, k))

def merge(s0, s1):
    """Return a stream over the elements of strictly increasing s0 and s1,
    removing repeats. Assume that s0 and s1 have no repeats.

    >>> ints = make_integer_stream(1)
    >>> twos = scale_stream(ints, 2)
    >>> threes = scale_stream(ints, 3)
    >>> m = merge(twos, threes)
    >>> stream_to_list(m, 10)
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    if s0 is Stream.empty:
        return s1
    elif s1 is Stream.empty:
        return s0

    e0, e1 = s0.first, s1.first

    if e0 == e1:
        return Stream(e0, lambda: merge(s0.rest, s1.rest))
    elif e0 < e1:
        return Stream(e0, lambda: merge(s0.rest, s1))
    else:
        return Stream(e1, lambda: merge(s1.rest, s0))

def make_s():
    """Return a stream over all positive integers with only factors 2, 3, & 5.

    >>> s = make_s()
    >>> stream_to_list(s, 20)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    """
    def rest():
        twos_and_threes = merge(scale_stream(s, 2), scale_stream(s, 3))
        fives = scale_stream(s, 5)
        return merge(twos_and_threes, fives)
    s = Stream(1, rest)
    return s


from operator import add, mul, mod


def make_random_stream(seed, a, c, n):
    """The infinite stream of pseudo-random numbers generated by the
    recurrence r[0] = SEED, r[i+1] = (r[i] * A + C) % N.  Your solution
    must not use any lambdas or def's that we have not supplied in the
    skeleton.
    >>> s = make_random_stream(25, 29, 5, 32)
    >>> stream_to_list(s, 10)
    [25, 26, 23, 0, 5, 22, 3, 28, 17, 18]
    >>> s = make_random_stream(17, 299317, 13, 2**20)
    >>> stream_to_list(s, 10)
    [17, 894098, 115783, 383424, 775373, 994174, 941859, 558412, 238793, 718506]
    """
    def compute_rest(r):
        r = (r * a + c) % n
        return Stream(r, lambda: compute_rest(r))
    return Stream(seed, lambda: compute_rest(seed))


def make_stream_of_streams():
    """
    >>> stream_of_streams = make_stream_of_streams()
    >>> stream_of_streams
    Stream(Stream(1, <...>), <...>)
    >>> stream_to_list(stream_of_streams, 3)
    [Stream(1, <...>), Stream(2, <...>), Stream(3, <...>)]
    >>> stream_to_list(stream_of_streams, 4)
    [Stream(1, <...>), Stream(2, <...>), Stream(3, <...>), Stream(4, <...>)]
    """
    "*** YOUR CODE HERE ***"
