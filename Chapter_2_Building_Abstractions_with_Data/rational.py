def rational(n, d):
	return [n, d]
	
def numer(x):
	return x[0]
	
def denom(x):
	return x[1]
	
def rationals_are_equal(x, y):
	return numer(x) * denom(y) == numer(y) * denom(x)
	
def print_rational(x):
	print(numer(x), '/', denom(x))
	
def mul_rationals(x, y):
	return rational(numer(x) * numer(y), denom(x) * denom(y))
	
def add_rationals(x, y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx * dy + ny * dx, dx * dy)	