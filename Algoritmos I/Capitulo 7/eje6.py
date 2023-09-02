def menores_y_mayores_a_k(lista, k):
	menores = []
	mayores = []
	iguales = []
	for i in lista:
		if i < k:
			menores.append(i)
		elif i > k:
			mayores.append(i)
		else:
			iguales.append(i)
	return (menores, mayores, iguales)
print(menores_y_mayores_a_k([1,2,3,4,5,43,546,3,3,3], 3))

def multiplo_de_k(lista, k):
	nueva_lista = []
	for i in lista:
		if i % k == 0:
			nueva_lista.append(i)
	return nueva_lista
print(multiplo_de_k([3,6,5,3,12,5,65,6,7,543,4], 3))			