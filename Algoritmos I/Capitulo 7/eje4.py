def prod_esc(u, v):
	total = 0
	for i in range(len(u)):
		total += u[i] * v[i]
	return total

def ortogonales(u, v):
	if prod_esc(u, v) == 0:
		return True
	else:
		return False
def paralelos(u, v):
	for i in range(len(u)):
		if multiplo_de(v, u) or multiplo_de(u, v):
			return True
	return False		
def multiplo_de(num1, num2):
	i = 2
	while num2 * i <= num1:
 		if num2 * i == num1:
 			return True
 		num2 *= i
	return False
def norma(u):
	radicando = 0
	for i in u:
		radicando += i**2
	return radicando**0.5	
print(norma((3,4)))	