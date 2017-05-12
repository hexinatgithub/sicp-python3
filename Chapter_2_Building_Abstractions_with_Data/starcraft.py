def make_unit(catchphrase, damage):
	return [catchphrase, damage]
	
def get_catchphrase(unit):
	return unit[0]
	
def get_damage(unit):
	return unit[1]

def battle(first, second):
	print(get_catchphrase(first))
	print(get_catchphrase(second))
	return first if get_damage(first) > get_damage(second) else second

def pair(x, y):
	"""Return a function that represents a pair."""
	def get(i):
		if i == 0:
			return x
		elif i == 1:
			return y
	return get
	
def select(p, i):
	"""Return the element at index i of pair p"""
	return p(i)

def make_resource_bundle(minerals, gas):
	return pair(minerals, gas)
	
def get_minerals(bundle):
	return select(bundle, 0)
	
def get_gas(bundle):
	return select(bundle, 1)
	
def make_building(unit, bundle):
	return pair(unit, bundle)
	
def get_unit(building):
	return select(building, 0)
	
def get_bundle(building):
	return select(building, 1)
	
def build_unit(building, bundle):
	"""Constructs a unit if given the minimum amount of
	resources. Otherwise, prints an error message.
	>>> barracks = make_building(make_unit(’Go go go!’, 6),
	... make_resource_bundle(50, 0))
	>>> marine = build_unit(barracks, make_resource_bundle(20,
	20))
	We require more minerals!
	>>> marine = build_unit(barracks, make_resource_bundle(50,
	0))
	>>> print(get_catchphrase(marine))
	Go go go!
	"""
	build_resource = get_bundle(building)
	if get_minerals(build_resource) > get_minerals(bundle):
		print("We require more minerals!")
		return
	if get_gas(build_resource) > get_gas(bundle):
		print("We require more vespene gas!")
		return
	return make_building(get_unit(building), get_bundle(building))
	