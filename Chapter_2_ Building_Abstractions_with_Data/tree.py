def tree(root, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root] + list(branches)
	
def root(tree):
	return tree[0]
	
def branches(tree):
	return tree[1:]
	
def is_tree(tree):
	if type(tree) != list and len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True
	
def is_leaf(tree):
	return not branches(tree)
	
def fib_tree(n):
	if n == 0 or n == 1:
		return tree(n)
	else:
		left, right = fib_tree(n-1), fib_tree(n-2)
		fib_n = root(left) + root(right)
		return tree(fib_n, [left, right])
		
def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		branch_counts = [count_leaves(b) for b in branches(tree)]
		return sum(branch_counts)
		
def partition_tree(n, m):
	if n == 0:
		return tree(True)
	elif n < 0 or m == 0:
		return tree(False)
	else:
		left, right = partition_tree(n-m, m), partition_tree(n, m-1)
		return tree(m, [left, right])
		
def print_partition_tree(tree, partition=[]):
	if is_leaf(tree):
		if root(tree):
			print(' + '.join(partition))
	else:
		left, right = branches(tree)
		m = str(root(tree))
		print_partition_tree(left, partition + [m])
		print_partition_tree(right, partition)
	