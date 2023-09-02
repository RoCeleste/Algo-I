def wc(archivo):
	with open(archivo, "r") as f:
		total_palabras = 0
		total_lineas = 0
		total_caracteres = 0
		for i in f:
			total_lineas += 1
			total_palabras += len(i.split())
			total_caracteres += len(i)
		print(f"{total_lineas} lineas, {total_palabras} palabras, {total_caracteres} caracteres")
