def n_lineas(archivo, n):
	with open(archivo, "r") as f:
		for i in range(n):
			print(f.readline(), end="")
