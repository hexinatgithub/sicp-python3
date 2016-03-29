def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess

def approx_eq(x, y, tolerance=1e-15):
	return abs(x - y) < tolerance

def average(x, y):
	return (x + y) / 2

def sqrt(a):
	def sqrt_update(x):
		return average(x, a/x)
	def sqrt_close(x):
		return approx_eq(x * x, a)
	return improve(sqrt_update, sqrt_close)

print(sqrt(4))