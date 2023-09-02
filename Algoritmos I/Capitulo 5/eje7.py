def suma_divisores(num):
	total = 0
	for i in range(2,num):
		if num % i == 0:
			total += i
			num = num / i
	return total + 1
def perfectos(m):
	for i in range(1, m+1):

		if i == suma_divisores(i):
			print(i)
def amigos(m):
	for i in range(1, m+1):
		for j in range(1,m):
			if suma_divisores(j) == suma_divisores(i):
				print((i,j))
# una posible optimizacion es descartar los primos y calcular suma_divisores() previamente y si el numero a evaluar es menor a sumar_divisores(), saltearlo porque la suma de los divisores no puede ser mayor al numero en si.				