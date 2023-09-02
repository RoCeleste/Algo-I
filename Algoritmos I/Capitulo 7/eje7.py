def nombres_en_cadena(lista_de_tuplas):
	nueva_lista = []
	for i in lista_de_tuplas:
		nueva_lista.append(f"{i[1]} {i[2]}. {i[0]}")
	return nueva_lista
	
print(nombres_en_cadena([("Marquez", "Eugenia", "I"),("Martinez", "Helena", "A")]))		