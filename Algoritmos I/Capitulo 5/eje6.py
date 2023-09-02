def es_potencia_de_dos(num):
	i = 1
	while 2**i <= num:
		if int(2**i) == num:
			
			return True
		i=i+1
			
	return False		

def potencias_acotadas(inf, sup):
	i=1
	suma = 0
	while 2**i < sup:
		if 2**i > inf and 2**i < sup:
			suma += 2**i
		i+=1
	return suma
print(potencias_acotadas(30, 500))			