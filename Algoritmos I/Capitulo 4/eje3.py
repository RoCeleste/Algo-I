def matriz_identidad(num):
	for x in range(1, num + 1):
		for y in range(1, num + 1):
			if x == y:
				print(1, end=" ")
			else:
				print(0, end=" ")
		print("")		
