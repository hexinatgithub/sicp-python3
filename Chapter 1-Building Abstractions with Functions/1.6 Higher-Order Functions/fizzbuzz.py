def fizzbuzz(n):
	"""
	>>> result = fizzbuzz(16)
	1
	2
	fizz
	4
	buzz
	fizz
	7
	8
	fizz
	buzz
	11
	fizz
	13
	14
	fizzbuzz
	16
	>>> result is None
	True
	"""
	current = 1
	while current <= n:
		if (current % 3 == 0) and (current % 5) == 0:
			print("fizzbuzz")
		elif current % 3 == 0:
			print("fizz")
		elif current % 5 == 0:
			print("buzz")
		else:
			print(current)
		current = current + 1