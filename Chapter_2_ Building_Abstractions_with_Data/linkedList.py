empty = 'empty'

def is_link(s):
	return s == empty or (len(s) == 2 and is_link(s[1]))
	
def link(first, rest):
	assert is_link(rest)
	return [first, rest]
	
def first(s):
	assert is_link(s)
	return s[0]
	
def rest(s):
	assert is_link(s)
	assert s != empty
	return s[1]
	
def len_link(s):
	length = 0
	while s != empty:
		s, length = rest(s), length + 1
	return length
	
def getitem_link(s, i):
	while i > 0:
		s, i = rest(s), i - 1
	return first(s)
	

def len_link_recursive(s):
	if s == empty:
		return 0
	else:
		return 1 + len_link_recursive(rest(s))
		
def getitem_link_recursive(s, i):
	if i == 0:
		return first(s)
	else:
		return getitem_link_recursive(s, i - 1)
		
def extend_link(s, t):
	"""Return a list with the elements of s followed by those of t."""
	assert is_link(s) and is_link(t)
	if s == empty:
		return t
	else:
		return link(first(s), extend_link(rest(s), t))
		
def apply_to_all_link(f, s):
	assert is_link(s)
	if s == empty:
		return s
	else:
		return link(f(first(s)), apply_to_all_link(f, rest(s)))
		
def keep_if_link(f, s):
	assert is_link(s)
	if s == empty:
		return s
	else:
		kept = keep_if_link(f, rest(s))
		if f(first(s)):
			return link(first(s), kept)
		else:
			return kept
			
def join_link(s, separator):
	if s == empty:
		return ''
	elif rest(s) == empty:
		return str(first(s))
	else:
		return str(first(s)) + separator + join_link(rest(s), separator)
		
def partitions(n, m):
	if n == 0:
		return link(empty, empty)
	elif n < 0 or m == 0:
		return empty
	else:
		using_m = partitions(n-m, m)
		with_m = apply_to_all_link(lambda x: link(m, x), using_m)
		without_m = partitions(n, m-1)
		return extend_link(with_m, without_m)

def print_partitions(n, m):
	lists = partitions(n, m)
	strings = apply_to_all_link(lambda s: join_link(s, ' + '), lists)
	print(join_link(strings, '\n'))