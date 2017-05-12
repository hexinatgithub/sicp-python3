from math import gcd
def make_rat(n, d):
	g = gcd(n, d) if d > 0 else -gcd(n, d)
	return n // g, d // g
	
def number(r):
	return r[0]
	
def denom(r):
	return r[1]