def closer_city(lat, lon, city1, city2):
	a = make_city("", lat, lon)
	return get_name(city1 if distance(a, city1) <= distance(a, city2) else city2)
	
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