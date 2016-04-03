def cascade(n):
	print(n)
	if n >= 10:
		cascade(n//10)
		print(n)

#cascade(233431)

def is_event(n):
	return n % 2 == 0

def play_alice(n):
	if n == 0:
		print("Bob win!")
	else:
		play_bob(n-1)

def play_bob(n):
	if n == 0:
		print("Alice win!")
	else:
		if is_event(n):
			play_alice(n-2)
		else:
			play_alice(n-1)

def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

def count_partitions(n, m):
	if n == 0:
	    return 1
	elif n < 0:
	    return 0
	elif m == 0:
	    return 0
	else:
		return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(20,20))












