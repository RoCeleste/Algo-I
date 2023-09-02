def tuplas_a_diccionario(lista_de_tuplas):
	dic = {}
	for i in lista_de_tuplas:
		if i[0] in dic:
			dic[i[0]].append(i[1])
		else:
			nueva_lista = []
			nueva_lista.append(i[1])
			dic[i[0]] = nueva_lista
	return dic		
