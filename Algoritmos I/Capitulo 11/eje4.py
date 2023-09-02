def grep(archivo, cadena):
	with open(archivo, "r") as f:
		for i in f:
			if cadena in i:
				print(i)