def negate(f, x):
	return -f(x)

def keep_ints(cond, n):
	current = 1
	while current <= n:
		if cond(current):
			print(current)
		current = current + 1

def keep_ints_hof(n):
	"""
	>>> def is_even(x):
	...     # Even numbers have remainder 0 when divided by 2.
	...     return x % 2 == 0
	>>> keep_ints_hof(5)(is_even)
	2
	4
	"""
	def f(cond):
		current = 1
		while current <= n:
			if cond(current):
				print(current)
			current = current + 1
	return f