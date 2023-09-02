def num_pares_acotados(min, max):
	if min % 2 == 0:
		for x in range(min, max+1, 2):
			print(x)
	else:
		for x in range(min+1, max+1, 2):
			print(x)
