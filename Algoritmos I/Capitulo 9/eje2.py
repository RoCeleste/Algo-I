import random

def contar_palabras(texto):
	dic = {}
	texto = texto.lower()
	palabras = texto.split()
	for palabra in palabras:
		if palabra in dic:
			dic[palabra] += 1
		else:
			dic[palabra] = 1
	return dic
def contar_caracteres(texto):
	dic = {}
	texto = texto.lower()
	for caracter in texto:
		if caracter == " " or not caracter.isalpha():
			continue
		if caracter in dic:
			dic[caracter] += 1
		else:
			dic[caracter] = 1
	return dic	
def tirada_de_dados(veces):
	dic = {}
	for i in range(veces):
		dado1 = random.randint(1, 6)
		dado2 = random.randint(1, 6)
		if str(dado1 + dado2) in dic:
			dic[str(dado1 + dado2)] += 1
		else:
			dic[str(dado1 + dado2)] = 1
	return dic		
