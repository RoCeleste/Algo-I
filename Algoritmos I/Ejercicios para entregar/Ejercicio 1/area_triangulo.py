import vectores

def area_triangulo(ux, uy, uz, vx, vy, vz, wx, wy, wz):
	"""Calcula el area de un triangulo dados 2 vectores"""
	# resta de vectores
	uv = vectores.diferencia(ux, uy, uz, vx, vy, vz)
	uw = vectores.diferencia(ux, uy, uz, wx, wy, wz)

	# asignacion a variable de cada componente de los vectores
	uvx, uvy, uvz = uv
	uwx, uwy, uwz = uw

	prod_vec = vectores.prod_vect(uvx, uvy, uvz, uwx, uwy, uwz)
	prod_vec_x , prod_vec_y, prod_vec_z = prod_vec
	norma_vec = vectores.norma(prod_vec_x, prod_vec_y, prod_vec_z)

	# el area del triangulo es la mitad del area del paralelogramo obtenido con el producto vectorial
	area = norma_vec / 2
	return area

assert area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == 19.45507645834372
assert area_triangulo(1, 0, 0, 5, 1, 0, 2, 0, 1) == 2.1213203435596424
assert area_triangulo(3, 1, 5, 0, -3, 2, -1, 1, 4) == 9.394147114027968


