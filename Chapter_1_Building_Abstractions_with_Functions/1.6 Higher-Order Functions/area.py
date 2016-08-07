from math import pi, sqrt

def area(r, shapeOfConstant):
	assert r > 0, "A length must be positive"
	return r * r * shapeOfConstant

def area_square(r):
	return area(r, 1)

def area_circle(r):
	return area(r, pi)

def area_hexagon(r):
	return area(r, 3 * sqrt(3) / 2)

print(area_circle(-4))