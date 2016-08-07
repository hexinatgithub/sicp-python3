"""Lab 2: Higher Order Functions & Lambdas & Recursions"""

def lambda_curry2(func):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)

def adder(f1, f2):
    """
    Return a function that takes in a single variable x, and returns
    f1(x) + f2(x). You can assume the result of f1(x) and f2(x) can be
    added together, and they both take in one argument.

    >>> identity = lambda x: x       # returns inpuSettingst
    >>> square = lambda x: x**2
    >>> a1 = adder(identity, square) # x + x^2
    >>> a1(4)
    20
    >>> a2 = adder(a1, identity)     # (x + x^2) + x
    >>> a2(4)
    24
    >>> a2(5)
    35
    >>> a3 = adder(a1, a2)           # (x + x^2) + (x + x^2 + x)
    >>> a3(4)
    44
    """
    return lambda x: f1(x) + f2(x)

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i <= n:
            print(i)
            counter(i+1)
    counter(1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a < b:
        a, b = b, a # a is lager number and b is smaller number
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
