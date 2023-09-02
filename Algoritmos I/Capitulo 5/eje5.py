m = int(input("Ingresa el primer numero"))
n = int(input("Ingresa el segundo numero"))
r = -1
while r != 0:
	r = m/n
	n = m
	r = n
print(n)	
