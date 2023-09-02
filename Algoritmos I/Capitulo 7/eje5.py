def lista_de_primos(lista):
	nueva_lista = []
	for i in lista:
		if primo(i) == "primo" and i != 1:
			nueva_lista.append(i)
	return nueva_lista		
def primo(num):
	if num == 2:
		return "primo"
	if num % 2 == 0:
		return "multiplo"
	for x in range(3, int(num / 2), 2):
		if num % x == 0:
			return "multiplo"
	return "primo"
print(lista_de_primos([1,2,3,4,45,6,7,8,9,10]))
def suma_y_promedio(lista):

	return (sum(lista), sum(lista)/len(lista))
print(suma_y_promedio([1,2,3,4]))

def factorial_de_lista(lista):
	nueva_lista = []
	for i in lista:
		nueva_lista.append(factorial(i))
	return nueva_lista	

def factorial(num):
	total = 1
	for x in range(1, num + 1):
		total = total * x
	return total	
print(factorial_de_lista([1,2,6,4]))	