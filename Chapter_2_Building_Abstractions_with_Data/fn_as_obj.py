from math import gcd

def make_rat(n, d):
	g = gcd(n, d) if d > 0 else -gcd(n, d)
	n = n // g; d = d // g
	return lambda which: n if which == 0 else d
	
def number(r):
	return r(0)
	
def denom(r):
	return r(1)
	
def add_rat(x, y):
	n, d = number(x) * denom(y) + number(y) * denom(x), denom(x) * denom(y)
	return make_rat(n, d)
	
def mul_rat(x, y):
	n, d = number(x) * number(y), denom(x) * denom(y)
	return make_rat(n, d)
	
