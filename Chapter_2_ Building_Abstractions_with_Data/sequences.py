def divisors(n):
	return [x for x in range(1, n) if n % x == 0]
	
def width(area, h):
	assert area % h == 0
	return area // h

def perimeter(width, height):
	return 2 * width + 2 * height
	
def minimum_perimeter(area):
	heights = divisors(area)
	perimeters = [perimeter(width(area, h), h) for h in heights]
	return min(perimeters)
	
def apply_to_all(map_fn, s):
	return [map_fn(x) for x in s]
	
def keep_if(filter_fn, s):
	return [x for x in s if filter_fn(x)]
	
def reduce(reduce_fn, s, initial):
	reduced = initial
	for item in s:
		reduced = reduce_fn(reduced, item)
	return reduced
	
def divisors_of(n):
	divisors_n = lambda x: n % x == 0
	return [1] + keep_if(divisors_n, range(2, n))
	
from operator import add

def sum_of_divisors(n):
	return reduce(add, divisors_of(n), 1)
	
def perfect(n):
	return sum_of_divisors(n) == n