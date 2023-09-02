def mensaje(tupla, p ,n):
	for i in range(p,p + n):
		if tupla[i][1] == "hombre":
			print(f"Estimado {tupla[i][0]}, vote por mi")
		elif tupla[i][1] == "mujer":
			print(f"Estimada {tupla[i][0]}, vote por mi")
		else:
			print(f"Estimade {tupla[i][0]}, vote por mi")	
mensaje((("Alenjandro", "hombre"), ("Eugenia", "no binarie"), ("Ludmila", "mujer"), ("Nora", "mujer"), ("Melina", "mujer"), ("Fabian", "hombre"), ("Ramiro", "no binarie")), 3, 4)