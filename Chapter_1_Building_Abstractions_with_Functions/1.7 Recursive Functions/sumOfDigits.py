def split(n):
	return n // 10, n % 10

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return last + sum_digits(all_but_last)

def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(n) + last

def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_digit = sum_digits(2 * last)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit

