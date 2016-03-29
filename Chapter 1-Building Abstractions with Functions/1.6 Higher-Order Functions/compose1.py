def square(x):
	return x * x

def successor(x):
	return x + 1

def compose1(f, g):
	def h(x):
		return f(g(x))
	return h

square_successor = compose1(square, successor)
print(square_successor(2))